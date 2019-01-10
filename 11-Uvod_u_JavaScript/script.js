function createParagraph() {
    let para = document.createElement('h3');
    para.textContent = 'Kliknuo si botun!';
    document.body.appendChild(para);
}

const buttons = document.querySelectorAll('button');

for (let i = 0; i < buttons.length; i++) {
    buttons[i].addEventListener('click', createParagraph);
}