let answer = document.querySelectorAll('.answer');

answer.forEach(function(answer) {

    let show_comments_btn = answer.childNodes[9];
    let hide_comments_btn = answer.childNodes[11];
    let comments = answer.childNodes[13];

    show_comments_btn.onclick = function(){
        comments.style.display = 'block';
        this.style.display = 'none';
        hide_comments_btn.style.display = 'block';
    }
    
    hide_comments_btn.onclick = function(){
        comments.style.display = 'none';
        this.style.display = 'none';
        show_comments_btn.style.display = 'block';
    }

})


