window.onload = on_load()
function on_load() {
    document.getElementById('nav_close').onclick = hide;
    document.getElementById('nav_next').onclick = next;
    document.getElementById('nav_prev').onclick = prev
}

function popup(img) {
    let LB = document.querySelector('#lightbox')
    LB.className = 'shown'
    img = document.getElementById(img)
    img.className = 'visible'
}

function hide() {
    document.getElementById('lightbox').setAttribute('class', 'hidden')
    let LB = document.querySelector('#lightbox')
    imgs = document.querySelectorAll('#lightbox > img.visible')
    for (let elem of LB.children) {
        elem.className = 'transparent'
    }
}

function next() {
    img = document.querySelector('img.visible')
    n_img = img.nextElementSibling
    if (n_img != document.getElementById("lb_nav")) {
        img.className = 'transparent'
        n_img.className = 'visible';
    }
}

function prev() {
    img = document.querySelector('img.visible')
    n_img = img.previousElementSibling
    if (img != document.getElementById('lightbox').firstElementChild) {
        img.className = 'transparent'
        n_img.className = 'visible'
    }
}