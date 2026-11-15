(function(){
var D=document,H=D.documentElement,W=window;
var RM=matchMedia('(prefers-reduced-motion:reduce)').matches;
var I18N={en:{t:'Akrivi (Vivi) Kopanitsanou | Art Psychotherapist, Neo Psychiko Athens',d:'Akrivi (Vivi) Kopanitsanou, certified Art Psychotherapist (ECP-h) and Mental Health Counsellor, M.Sc., in Neo Psychiko, Athens. Children, adolescents, adults and groups.'},el:{t:D.title,d:''}};
/* ---------- language ---------- */
var KEY='kop-lang',cur='el';
function swap(l){
  if(l===cur)return;
  D.querySelectorAll('[data-en]').forEach(function(e){if(!e.hasAttribute('data-el'))e.setAttribute('data-el',e.innerHTML);e.innerHTML=l==='en'?e.getAttribute('data-en'):e.getAttribute('data-el')});
  [['data-en-alt','alt'],['data-en-aria','aria-label']].forEach(function(p){D.querySelectorAll('['+p[0]+']').forEach(function(e){var k='data-el-'+p[1];if(!e.hasAttribute(k))e.setAttribute(k,e.getAttribute(p[1])||'');e.setAttribute(p[1],l==='en'?e.getAttribute(p[0]):e.getAttribute(k))})});
  H.lang=l;cur=l;D.title=l==='en'?I18N.en.t:I18N.el.t;
  D.querySelectorAll('.fl').forEach(function(b){b.classList.toggle('on',b.getAttribute('data-l')===l);b.setAttribute('aria-pressed',b.getAttribute('data-l')===l)});
  D.querySelectorAll('.lc').forEach(function(h){h.removeAttribute('data-lc');split(h);h.classList.add('in')});
}
D.querySelectorAll('.fl').forEach(function(b){b.addEventListener('click',function(){var l=b.getAttribute('data-l');try{localStorage.setItem('kop-lang',l)}catch(e){}swap(l)})});
var saved;try{saved=localStorage.getItem(KEY)}catch(e){}
D.querySelectorAll('.fl').forEach(function(b){b.classList.toggle('on',b.getAttribute('data-l')==='el')});
/* ---------- heading splits ---------- */
function split(h){
  if(h.dataset.lc)return;h.dataset.lc=1;var fx=h.getAttribute('data-fx')||'c',i=0;
  h.setAttribute('aria-label',h.textContent.replace(/\s+/g,' ').trim());
  (function walk(n){Array.prototype.slice.call(n.childNodes).forEach(function(c){
    if(c.nodeType===3){var f=D.createDocumentFragment();c.textContent.split(/(\s+)/).forEach(function(w){if(!w)return;if(/^\s+$/.test(w)){f.appendChild(D.createTextNode(' '));return}
      var s=D.createElement('span');s.setAttribute('aria-hidden','true');
      if(fx==='rise'){s.className='lc-m';var t=D.createElement('span');t.className='lc-mi';t.style.setProperty('--i',i++);t.textContent=w;s.appendChild(t)}
      else if(fx==='light'){s.className='lc-l';s.style.setProperty('--i',i++);s.textContent=w}
      else{s.className='lc-w';Array.from(w).forEach(function(ch){var x=D.createElement('span');x.className='lc-c';x.style.setProperty('--i',i++);x.textContent=ch;s.appendChild(x)})}
      f.appendChild(s)});c.replaceWith(f)}
    else if(c.nodeType===1&&c.tagName!=='BR')walk(c)})})(h);
}
if(saved==='en')swap('en');
if(!RM)D.querySelectorAll('.lc').forEach(split);
/* ---------- intro ---------- */
var introOn=H.classList.contains('js-intro');
function start(){H.classList.add('ready')}
if(introOn&&!RM&&!D.hidden){
  var it=D.getElementById('intro');
  setTimeout(function(){it.classList.add('go');setTimeout(start,280)},1500);
  setTimeout(function(){it.style.display='none';H.classList.remove('js-intro')},2700);
  try{sessionStorage.setItem('kop-intro','1')}catch(e){}
}else{H.classList.remove('js-intro');requestAnimationFrame(start)}
setTimeout(start,3200);
/* ---------- reveal ---------- */
var REV='.kick,.lc,.ink,.about-ph,.sig,.fr,.sv,.svc-int,.g,.icps,.tl-i,.score,.rv,.qa,.ct-list,.ct-map,.ct-cta,.proof';
var els=D.querySelectorAll(REV);
if(RM||!('IntersectionObserver' in W)){els.forEach(function(e){e.classList.add('in')})}
else{var io=new IntersectionObserver(function(es){es.forEach(function(e){if(!e.isIntersecting)return;var t=e.target;t.classList.add('in');
  if(t.classList.contains('ct-cta'))t.classList.add('pulse');
  if(t.classList.contains('proof'))count();
  if(!t.classList.contains('ink'))io.unobserve(t)})},{rootMargin:'0px 0px -8% 0px',threshold:.04});
  els.forEach(function(e){if(!e.classList.contains('ink'))io.observe(e)});
  var io2=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io2.unobserve(e.target)}})},{rootMargin:'0px 0px -30% 0px'});
  D.querySelectorAll('.ink').forEach(function(e){io2.observe(e)});
  D.querySelectorAll('.rv').forEach(function(e,k){e.style.setProperty('--i',k%3)});
}
function count(){D.querySelectorAll('.cnt').forEach(function(c){var to=+c.dataset.to;if(RM||D.hidden){c.textContent=to;return}var t0=performance.now();c.textContent='7';
  (function f(t){var p=Math.min(1,(t-t0)/1200);c.textContent=Math.round(7+(to-7)*(1-Math.pow(1-p,3)));if(p<1)requestAnimationFrame(f)})(t0);setTimeout(function(){c.textContent=to},1600)})}
/* ---------- pause off-screen ambient ---------- */
if('IntersectionObserver' in W){var io3=new IntersectionObserver(function(es){es.forEach(function(e){e.target.classList.toggle('off',!e.isIntersecting)})});D.querySelectorAll('.hero,.dark,.tick').forEach(function(e){io3.observe(e)})}
/* ---------- scroll: header, progress, scene, timeline ---------- */
var hd=D.getElementById('hd'),prog=D.getElementById('prog'),tt=D.getElementById('totop'),mb=D.getElementById('mbar'),ttP=D.getElementById('ttP');
var scene=D.getElementById('scene'),svg=scene&&scene.querySelector('.sc-svg'),steps=scene?scene.querySelectorAll('.sc-st'):[],tl=D.getElementById('tl'),tli=tl?tl.querySelectorAll('.tl-i'):[];
var ticking=false;
function clamp(x){return x<0?0:x>1?1:x}
function onScroll(){ticking=false;var y=W.scrollY,vh=W.innerHeight,dh=H.scrollHeight-vh,p=dh>0?y/dh:0;
  hd.classList.toggle('solid',y>40);H.classList.toggle('scrolled',y>80);
  prog.style.transform='scaleX('+p+')';
  if(tt){tt.classList.toggle('on',y>vh*.9);ttP.style.setProperty('--tt',1-p)}
  if(mb)mb.classList.toggle('on',y>vh*.55);
  if(scene&&svg){var r=scene.getBoundingClientRect(),q=clamp((vh*.55-r.top)/(r.height-vh*.35));
    var a=clamp(q/.24),b=clamp((q-.33)/.24),c=clamp((q-.66)/.22);
    var s=svg.style;s.setProperty('--s1',1-a);s.setProperty('--o1',b>0?1-b:1);s.setProperty('--s2',1-b);s.setProperty('--o2',c>0?1-c*1.2:1);s.setProperty('--f2',b>.6?1:0);s.setProperty('--s3',1-c);s.setProperty('--f3',c>.4?1:0);s.setProperty('--b',c);
    var k=q<.34?0:q<.66?1:2;steps.forEach(function(st,j){st.classList.toggle('on',j===k)})}
  if(tl){var tr=tl.getBoundingClientRect(),tp=clamp((vh*.6-tr.top)/tr.height);tl.style.setProperty('--tp',tp);
    tli.forEach(function(li){li.classList.toggle('on',li.getBoundingClientRect().top<vh*.6)})}
}
W.addEventListener('scroll',function(){if(!ticking){ticking=true;requestAnimationFrame(onScroll)}},{passive:true});
W.addEventListener('resize',onScroll);onScroll();
if(tt)tt.addEventListener('click',function(){W.scrollTo({top:0,behavior:RM?'auto':'smooth'})});
/* ---------- mobile nav ---------- */
var bg=D.getElementById('burger'),mn=D.getElementById('mnav'),mx=D.getElementById('mnavX');
function openN(){mn.hidden=false;requestAnimationFrame(function(){mn.classList.add('open')});bg.setAttribute('aria-expanded','true');D.body.style.overflow='hidden';mx.focus()}
function closeN(){mn.classList.remove('open');bg.setAttribute('aria-expanded','false');D.body.style.overflow='';setTimeout(function(){mn.hidden=true},350)}
bg.addEventListener('click',openN);mx.addEventListener('click',closeN);mn.querySelectorAll('a').forEach(function(a){a.addEventListener('click',closeN)});
/* ---------- services hover preview ---------- */
var pv=D.getElementById('svPrev');
if(pv&&matchMedia('(hover:hover) and (pointer:fine)').matches&&!RM){var pi=pv.querySelector('img'),x=0,yy=0,cx=0,cy=0,run=false;
  function tick(){cx+=(x-cx)*.16;cy+=(yy-cy)*.16;pv.style.transform='translate3d('+(cx+28)+'px,'+(cy-90)+'px,0) rotate('+((x-cx)*.03)+'deg)';if(Math.abs(x-cx)+Math.abs(yy-cy)>.4)requestAnimationFrame(tick);else run=false}
  D.querySelectorAll('.sv').forEach(function(sv){sv.addEventListener('mouseenter',function(e){pi.src=sv.dataset.img;pv.classList.add('on');x=cx=e.clientX;yy=cy=e.clientY});sv.addEventListener('mouseleave',function(){pv.classList.remove('on')});
    sv.addEventListener('mousemove',function(e){x=e.clientX;yy=e.clientY;if(!run){run=true;requestAnimationFrame(tick)}})})}
/* ---------- reviews ---------- */
var tr=D.getElementById('rvTrack'),bar=D.getElementById('rvBar');
if(tr){function upd(){var m=tr.scrollWidth-tr.clientWidth,f=tr.clientWidth/tr.scrollWidth;bar.style.width=(f*100)+'%';bar.style.transform='translateX('+(m>0?tr.scrollLeft/m*(1/f-1)*100:0)+'%)'}
  tr.addEventListener('scroll',upd,{passive:true});W.addEventListener('resize',upd);upd();
  D.querySelectorAll('.rv-b').forEach(function(b){b.addEventListener('click',function(){var c=tr.querySelector('.rv');tr.scrollBy({left:(+b.dataset.d)*(c.offsetWidth+22),behavior:RM?'auto':'smooth'})})})}
/* ---------- FAQ: one open ---------- */
D.querySelectorAll('.qa').forEach(function(d){d.addEventListener('toggle',function(){if(d.open)D.querySelectorAll('.qa').forEach(function(o){if(o!==d)o.open=false})})});
/* ---------- lightbox ---------- */
var lb=D.getElementById('lb'),lbi=D.getElementById('lbImg'),lbx=D.getElementById('lbX'),last;
function lbOpen(src,alt){last=D.activeElement;lbi.src=src;lbi.alt=alt||'';lb.hidden=false;requestAnimationFrame(function(){lb.classList.add('on')});lbx.focus()}
function lbClose(){lb.classList.remove('on');setTimeout(function(){lb.hidden=true;lbi.src=''},300);if(last)last.focus()}
D.querySelectorAll('.lb-t').forEach(function(b){b.addEventListener('click',function(){var im=b.querySelector('img');lbOpen(b.dataset.full,im&&im.alt)})});
lbx.addEventListener('click',lbClose);lb.addEventListener('click',function(e){if(e.target===lb)lbClose()});
D.addEventListener('keydown',function(e){if(e.key==='Escape'){if(!lb.hidden)lbClose();if(!mn.hidden)closeN()}});
})();
