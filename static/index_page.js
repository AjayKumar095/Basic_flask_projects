var taskButtons = document.getElementsByClassName('taskButton');
for (var i = 0; i < taskButtons.length; i++) {
    taskButtons[i].addEventListener('click', function() {
        var task = this.getAttribute('data-task');
        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/' + task, true);
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.onload = function() {
            if (xhr.status === 200) {
                document.getElementById('result').innerHTML = JSON.parse(xhr.responseText).result;
            }
        };
        xhr.send(JSON.stringify({}));
    });
}