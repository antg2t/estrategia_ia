const {chromium}=require(process.argv[2]);
const fs=require('node:fs');
const path=require('node:path');
const {pathToFileURL}=require('node:url');
const assert=require('node:assert/strict');
const root=path.resolve(__dirname,'../..');
const target=path.join(root,'outputs/segunda-feira/REUNIAO_ESTRATEGIA_IA_VP_PESSOAS.html');
const original=process.argv[3];
(async()=>{
 const browser=await chromium.launch({channel:'chrome',headless:true});
 const page=await browser.newPage({viewport:{width:1440,height:900}});
 const snapshots=[];
 for(const file of [original,target]){
  await page.goto(pathToFileURL(file).href+'#modo=estendido&quadro=encerramento');
  await page.evaluate(()=>document.fonts.ready);
  snapshots.push({data:await page.evaluate(()=>DATA.slides.find(s=>s.id==='encerramento')),body:await page.locator('#encerramento .vpp-content-layer').innerHTML(),png:await page.locator('#encerramento .vpp-stage').screenshot()});
 }
 assert.deepEqual(snapshots[0].data,snapshots[1].data);
 assert.equal(snapshots[0].body,snapshots[1].body);
 assert.ok(snapshots[0].png.equals(snapshots[1].png),'Final slide pixels must be identical');
 const report=await page.evaluate(()=>{
  const plain=el=>el.textContent.replace(/\s+/g,' ').trim();
  const by=Object.fromEntries(DATA.slides.map(s=>[s.id,s]));
  const issues=[];
  for(const id of ['apostas','execucao-mapa']){
   const buttons=[...document.querySelectorAll('#'+id+' [data-jump]')];
   for(const button of buttons){
    const dest=button.dataset.jump;
    const title=plain(button.querySelector('strong,h3'));
    if(title!==by[dest].title)issues.push(`${id}: ${title} != ${by[dest].title}`);
   }
   for(const [mode,route] of Object.entries(DATA.routes)){
    const expected=buttons.map(b=>b.dataset.jump);
    const actual=route.slice(route.indexOf(id)+1,route.indexOf(id)+1+expected.length);
    if(JSON.stringify(expected)!==JSON.stringify(actual))issues.push(`${mode}: ${id} order`);
   }
  }
  for(const button of document.querySelectorAll('[data-jump]'))if(!by[button.dataset.jump])issues.push('Missing destination '+button.dataset.jump);
  return {issues,finalSlide:'identical content, metadata and pixels',routes:Object.fromEntries(Object.entries(DATA.routes).map(([k,v])=>[k,v.length]))};
 });
 assert.deepEqual(report.issues,[]);
 fs.writeFileSync(path.join(root,'output/playwright/narrative-report.json'),JSON.stringify(report,null,2));
 console.log(JSON.stringify(report,null,2));
 await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
