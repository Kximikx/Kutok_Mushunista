document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('contact-form');

    form.addEventListener('submit', function(e) {
        e.preventDefault();

        const name = form.elements.name.value;
        const email = form.elements.email.value;
        const message = form.elements.message.value;

        // Тут ви можете додати код для відправки даних на сервер
        // Наприклад, використовуючи fetch API

        console.log('Form submitted:', { name, email, message });

        // Очистимо форму і покажемо повідомлення про успіх
        form.reset();
        alert('Дякуємо за ваше повідомлення! Ми зв\'яжемося з вами найближчим часом.');
    });
});

