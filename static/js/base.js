let darkMode = false;

function toggleMod() {
  let main = document.querySelector('body');

  if(!darkMode){
  main.style.backgroundColor = '#071e26';
  main.style.color = 'white';
  darkMode = true;
  }
  else{
  main.style.backgroundColor = '';
  main.style.color = '';
  darkMode = false;
  }
}




