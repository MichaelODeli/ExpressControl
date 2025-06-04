document.addEventListener('DOMContentLoaded', function() {
    function updateTime() {
        const now = new Date();
        const dateString = 
            String(now.getDate()).padStart(2, '0') + '.' +
            String(now.getMonth() + 1).padStart(2, '0') + '.' +
            now.getFullYear(); 
        const timeString = now.toLocaleTimeString();  
        
        document.getElementById('timeDisplay').innerText = dateString + ' ' + timeString; 
        document.getElementById('timeDisplay_manual').innerText = dateString + ' ' + timeString; 
    }

    setInterval(updateTime, 1000); // Обновляем каждую секунду
    updateTime(); // Сразу вызываем функцию для первоначального отображения
});