function popup(i) {
    document.getElementById('pic').setAttribute('src', i)
    document.getElementById('lightbox').setAttribute('class', 'shown');
    
}

function hide() {
    document.getElementById('lightbox').setAttribute('class', 'hidden')
}

function lb_next() {
    document.getElementById('pic').setAttribute('src', 'img/1.JPG')
}
function lb_prev() {
    document.getElementById('pic').setAttribute('src', 'img/3.JPG')
}
