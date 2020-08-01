//let body = document.querySelector('.body');
//let p = document.querySelector('.text');
//document.addEventListener('DOMContentLoaded', function(){
//  alert('asd');
//  body.style.visibility = 'visible';
//});
let menu = document.querySelector('.but');
let sub_menu = document.querySelector('.menu');

menu.addEventListener('mouseover', function(){
  setTimeout(function() {
    sub_menu.style.display = 'block'
  },100);
});

menu.addEventListener('mouseout', function(){
  setTimeout(function() {
    sub_menu.style.display = 'none'
  },100);
});


sub_menu.addEventListener('mouseover', function(){
  setTimeout(function() {
    sub_menu.style.display = 'block'
  },100);
});

sub_menu.addEventListener('mouseout', function(){
  setTimeout(function() {
    sub_menu.style.display = 'none'
  },100);
});

let note_window = document.querySelector('.note_window');
let qbody = document.querySelector('.body');
let show_b = false;



let q_card = document.querySelectorAll('.card');
q_card.forEach(function(item) {
  item.addEventListener('click', function() {
      show_b = true;
      this.classList.toggle("show_b");
  });
  item.addEventListener('click', function() {
    let ed_del = document.querySelectorAll('.edit_on_card');
    ed_del.style.opacity = '0.5';
  });
   });
/*
q_card.addEventListener('click', function(){
  qbody.style.background = '#242323';
  note_window.style.display = 'block';
  note_window.style.color = 'rgba(255, 255, 255, 1)';
  note_window.style.background = '#323131';

});

note_window.addEventListener('click', function(){
  note_window.style.display = 'none';
  qbody.style.background = '#323131';
});
*/
