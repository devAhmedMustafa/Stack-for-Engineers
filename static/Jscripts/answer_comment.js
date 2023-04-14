let answerDiv = document.querySelectorAll('.answer');

let answerField = document.querySelector('#answer_field');
let answerBtn = document.querySelector('#post_answer');


answerBtn.addEventListener('click', function() {
    let answer = answerField.value;
    let pk = parseInt(answerBtn.value)
    
    $.ajax({
        url: '/post_answer/',
        data: {'answer':answer, 'pk':pk},
        dataType: 'json',
        success: function(data) {

            if (data.status == 'success') {
                answerBtn.style.border = '1px solid green';
            }
        }
    })
})

answerDiv.forEach(function(div){
    let commentsDiv = div.querySelector('.comment_action');
    let commentField = commentsDiv.querySelector('.comment_field');
    let commentBtn =commentsDiv.querySelector('.post_comment');

    commentBtn.addEventListener('click', function() {
        let comment = commentField.value;
        let pk = parseInt(this.value);

        $.ajax({
            url: '/post_comment/',
            data: {'comment':comment, 'pk':pk},
            dataType: 'json',
            success: function(data) {
    
                if (data.status == 'success') {
                    commentBtn.style.bborder= '1px solid green';
                }
            }
        })
        
    })

})