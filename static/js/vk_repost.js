// Получаем все элементы <li> внутри <ul>
const blocks = document.querySelectorAll('.clickable-block');
const form = document.getElementById('post_form');

blocks.forEach(block => {
    block.addEventListener('click', function () {
        const titleInput = form.querySelector('#id_title');
        titleInput.value = block.querySelector('#vk_description').innerHTML.split(/[.,]+/)[0];
        const textInput = form.querySelector('#id_description');
        textInput.value = block.querySelector('#vk_description').innerHTML;
        const tags = form.querySelector('#id_tags');
        // tags.value = block.querySelector('#vk_description').innerHTML.split(/[., ]+/).filter(word => word.length > 2).map(word => word.toLowerCase()).join(', ');

        window.scrollTo(0, 0);
        // load files
        const images = block.querySelectorAll('a')
        addImagesToFileInput(images)

        // preview album
        const thumbnails = block.querySelectorAll('img')
        const album_block = document.querySelector('#album')
        thumbnails.forEach(thumbnail => {
            album_block.append(thumbnail);
        });
    });
});
// Функция для загрузки изображения по URL и преобразования его в File
async function fetchImageAsFile(imgUrl, fileName) {
    try {
        const response = await fetch(imgUrl);
        if (!response.ok) throw new Error('Ошибка при загрузке изображения');

        const blob = await response.blob(); // Получаем изображение как Blob
        return new File([blob], fileName, { type: blob.type }); // Преобразуем Blob в File
    } catch (error) {
        console.error('Не удалось загрузить изображение:', error);
        return null;
    }
}

// Функция для добавления файлов в input
async function addImagesToFileInput(images) {
    const files = [];
    const fileInput = form.querySelector('#id_image');
    const albumDiv = form.querySelector('#album'); // Получаем div

    // Очищаем file input
    fileInput.value = ''; // Очищаем значение
    const clearDataTransfer = new DataTransfer();
    fileInput.files = clearDataTransfer.files; // Очищаем FileList

    albumDiv.innerHTML = ''; // Удаляем всё содержимое

    // Собираем все изображения из блоков
    for (const a of images) {
        if (a && a.href) {
            const file = await fetchImageAsFile(a.href, a.id);
            if (file) files.push(file);
        }
    }

    // Создаём новый FileList и добавляем файлы в input
    const newDataTransfer = new DataTransfer();
    files.forEach(file => newDataTransfer.items.add(file));
    fileInput.files = newDataTransfer.files;

    console.log('Изображения добавлены в input:', fileInput.files);
}