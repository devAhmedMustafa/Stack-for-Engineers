let username = document.querySelector('#id_username');
let password1 = document.querySelector('#id_password1')
let password2 = document.querySelector('#id_password2')

let userHelpText = document.getElementsByTagName('span')[1]
let passwordHelpText1 = document.getElementsByTagName('span')[2]
let passwordHelpText2 = document.getElementsByTagName('span')[3]


username.onchange = function username_validation(){
    $.ajax({
        url: '/user_validation/',
        data: { 'username': username.value },
        dataType: 'json',
        success: function(data){
            if(data.is_taken){
                userHelpText.innerHTML = 'Username already taken';
                userHelpText.style.color = 'rgb(180, 0, 0)';
                username.style.borderColor = 'rgb(180, 0, 0)';
                username.style.color = 'rgb(180, 0, 0)';
                return false;
            }
            else{
                userHelpText.innerHTML = '';
                userHelpText.style.color = 'green';
                username.style.borderColor = 'green';
                username.style.color = 'black';
                return true;
            }
        }
    })
}

password1.onkeyup = function password_validation(){
    
    passvalue = password1.value;

    function styling(){
        passwordHelpText1.style.color = 'rgb(180, 0, 0)';
        password1.style.color = 'rgb(180, 0, 0)';
        password1.style.borderColor = 'rgb(180, 0, 0)';
    }

    if ( passvalue.length < 8 ){
        passwordHelpText1.innerHTML = 'Your password must contain at least 8 characters';
        styling();
        return false;
    }
    if ( passvalue.match(/'[a-z]'/) == false ){
        passwordHelpText1.innerHTML = 'Your password must contain at least one lowercase letter';
        styling();
        return false;
    }
    if ( passvalue.match(/'[A-Z]'/) == false ){
        passwordHelpText1.innerHTML = 'Your password must contain at least one uppercase letter';
        styling();
        return false;
    }
    if ( passvalue.match(/'[0-9]'/) == false ){
        passwordHelpText1.innerHTML = 'Your password must contain at least one number';
        styling();
        return false;
    }

    passwordHelpText1.innerHTML = '';
    passwordHelpText1.style.color = 'green';
    this.style.color = 'green';
    this.style.borderColor = 'green';
    return true;

}

password2.onkeyup = function password_matching(){

    passvalue = password2.value;
    
    if ( passvalue != password1.value ){
        passwordHelpText2.innerHTML = 'Passwords do not match';
        passwordHelpText2.style.color = 'rgb(180, 0, 0)';
        this.style.color = 'rgb(180, 0, 0)';
        this.style.borderColor = 'rgb(180, 0, 0)';
        return false;
    }
    else{
        passwordHelpText2.innerHTML = '';
        passwordHelpText2.style.color = 'green';
        this.style.color = 'green';
        this.style.borderColor = 'green';
        return true;
    }

}
