let questionContainer = document.querySelectorAll('.question');
let answerContainer = document.querySelectorAll('.answer');

answerContainer.forEach(async function(answer){

    let btnDiv = answer.querySelector('.comment_action').querySelector('.reaction');
    let pk = parseInt(answer.querySelector('.comment_action').querySelector('.post_comment').value);
    

    $.ajax({

        url: '/get_like_status/',
        dataType: 'json',
        data: {'pk':pk},
        success: function(data){
            btnDiv.innerHTML = `<button class="reactions" value="${data.likeStatus}"><img src="/static/SVGs/thumbs-up-${data.likeStatus}.svg" width="24px"></button>
            <input class='r' type='number' value="${pk}">`
        }

    })

    btnDiv.addEventListener('click', async function(){
        likeBtn = this.querySelector('.reactions')
        let status = likeBtn.value;
        let pk = parseInt(answer.querySelector('.like').querySelector('.reaction').querySelector('.r').value);
            $.ajax({
                url: '/api_answer_reaction/',
                dataType: 'json',
                data: {'status':status, 'pk':pk},
                success: function(){
                    if(status=='liked'){
                        likeBtn.querySelector('img').src = '/static/SVGs/thumbs-up-unliked.svg';
                        likeBtn.value = 'unliked';
                    }
                    else{
                        likeBtn.querySelector('img').src = '/static/SVGs/thumbs-up-liked.svg';
                        likeBtn.value = 'liked';
                    }
                }
            })
    })

})


questionContainer.forEach(function(question){

    saveBtn = question.querySelector('.saves');
    saveBtn.addEventListener('click', function(){
        let status = this.value;
        let pk = parseInt(question.querySelector('.like').querySelector('.s').value);
            
            $.ajax({
                url: '/api_saves/',
                dataType: 'json',
                data: {'status':status, 'pk':pk},
                success: function(){
                    if(status=='saved'){
                        saveBtn.querySelector('img').src = '/static/SVGs/bookmark-unsaved.svg';
                        saveBtn.value = 'unsaved';
                    }
                    else{
                        saveBtn.querySelector('img').src = '/static/SVGs/bookmark-saved.svg';
                        saveBtn.value = 'saved';
                    }
                }
            })
    })

    likeBtn = question.querySelector('.reactions');
    likeBtn.addEventListener('click', function(){
        let status = this.value;
        let pk = parseInt(question.querySelector('.like').querySelector('.r').value);
            
            $.ajax({
                url: '/api_reactions/',
                dataType: 'json',
                data: {'status':status, 'pk':pk},
                success: function(){
                    if(status=='liked'){
                        likeBtn.querySelector('img').src = '/static/SVGs/thumbs-up-unliked.svg';
                        likeBtn.value = 'unliked';
                    }
                    else{
                        likeBtn.querySelector('img').src = '/static/SVGs/thumbs-up-liked.svg';
                        likeBtn.value = 'liked';
                    }
                }
            })
    })


})

