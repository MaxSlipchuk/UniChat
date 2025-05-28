const formReg = document.getElementById('register-form');
formReg.addEventListener('submit', function(event) {
    event.preventDefault();
    console.log('Форма не була надіслана, перевірте дані.');

    const formData = new FormData(formReg);
    // Отримання CSRF-токена щоб уникнути помилки 403 Forbidden
    // CSRF-токен можна отримати з мета-тегу в HTML
    const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
    fetch('/users/login/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrfToken,
            'X-Requested-With': 'XMLHttpRequest'
        },
        body: formData
        
  })
    .then(response => response.json())
    .then(data => {
        console.log(data.success); // Успішно!
        if (data.success === true) {
            alert('Реєстрація успішна!');
            // window.location.href = '/users/login/';
        } else {
            console.log(data.errors); // Успішно!
            alert('Помилка реєстрації: ' + data.errors);
        }
    })
});