const form = document.getElementById('form');

const username = document.getElementById('username');

const email = document.getElementById('email');

const telefone = document.getElementById('telefone');

const cpf = document.getElementById('cpf');

const data = document.getElementById('data');

const genero = document.getElementById('genero');

const rua = document.getElementById('rua');

const numero = document.getElementById('numero');

const bairro = document.getElementById('bairro');

const cidade = document.getElementById('cidade');

const uf = document.getElementById('uf');

const cep = document.getElementById('cep');

const password = document.getElementById('password');

const passwordConfirmation = document.getElementById('password-confirmation');

form.addEventListener('submit', (event) => {
    event.preventDefault();

    checkForm();

    form.reset();
       
})

email.addEventListener('blur', () => {
    checkInputEmail();
});

telefone.addEventListener('blur', () => {
    checkInputTelefone();
});

username.addEventListener('blur', () => {   
    checkInputUsername();
});

cpf.addEventListener('blur', () => {
    checkInputCpf();
});

data.addEventListener('blur', () => {
    checkInputData ();
});

genero.addEventListener('blur', () => {
    checkInputGenero();
});

rua.addEventListener('blur', () => {
    checkInputRua();
});

numero.addEventListener('blur', () => {
    checkInputNumero();
});

bairro.addEventListener('blur', () => {
    checkInputBairro();
});

cidade.addEventListener('blur', () => {
    checkInputCidade();
});
uf.addEventListener('blur', () => {
    checkInputUf();
}); 

cep.addEventListener('blur', () => {
    checkInputCep();
});



password.addEventListener('blur', () => {
    checkInputPassword();
});
passwordConfirmation.addEventListener('blur', () => {
    checkInputPasswordConfirmation();
});   



function checkInputUsername() {
    const usernameValue = username.value;

    if (usernameValue === '') {
        errorInput(username, 'O nome de usuário é obrigatório')
    } else {
        const formItem = username.parentElement;
        formItem.className = 'form-content'
    }

}

  function checkInputEmail() {
        const emailValue = email.value;
    
        if (emailValue === '') {
            errorInput(email, 'O e-mail é obrigatório')
        } else {
            const formItem = email.parentElement;
            formItem.className = 'form-content'
        }
}


function checkInputTelefone() {
    const telefoneValue = telefone.value;

    if (telefoneValue === '') {
        errorInput(telefone, 'O telefone é obrigatório')
    } else {
        const formItem = telefone.parentElement;
        formItem.className = 'form-content'
    }
}   
function checkInputCpf() {
    const cpfValue = cpf.value;

    if (cpfValue === '') {
        errorInput(cpf, 'O CPF é obrigatório')
    } else {
        const formItem = cpf.parentElement;
        formItem.className = 'form-content'
    }
} 
function checkInputData () {
    const dataValue = data.value;

    if (dataValue === '') {
        errorInput(data, 'A data é obrigatória')
    } else {
        const formItem = data.parentElement;
        formItem.className = 'form-content'
    }
}   

function checkInputGenero() {
    const generoValue = genero.value;

    if (generoValue === '') {
        errorInput(genero, 'O gênero é obrigatório')
    } else {
        const formItem = genero.parentElement;
        formItem.className = 'form-content'
    }
}

function checkInputRua() {
    const ruaValue = rua.value;

    if (ruaValue === '') {
        errorInput(rua, 'A rua é obrigatória')
    } else {
        const formItem = rua.parentElement;
        formItem.className = 'form-content'
    }
}   

function checkInputNumero() {
    const numeroValue = numero.value;

    if (numeroValue === '') {
        errorInput(numero, 'N.º ?')
    } else {
        const formItem = numero.parentElement;
        formItem.className = 'form-content'
    }
}   

function checkInputBairro() {
    const bairroValue = bairro.value;

    if (bairroValue === '') {
        errorInput(bairro, 'O bairro é obrigatório')
    } else {
        const formItem = bairro.parentElement;
        formItem.className = 'form-content'
    }
}

function checkInputCidade() {
    const cidadeValue = cidade.value;

    if (cidadeValue === '') {
        errorInput(cidade, 'A cidade é obrigatória')
    } else {
        const formItem = cidade.parentElement;
        formItem.className = 'form-content'
    }
}

function checkInputUf() {
    const ufValue = uf.value;

    if (ufValue === '') {
        errorInput(uf, 'O estado')
    } else {
        const formItem = uf.parentElement;
        formItem.className = 'form-content'
    }
}

function checkInputCep() {
    const cepValue = cep.value;

    if (cepValue === '') {
        errorInput(cep, 'O CEP é obrigatório')
    } else {
        const formItem = cep.parentElement;
        formItem.className = 'form-content'
    }
}       


function checkInputPassword() {
    const passwordValue = password.value;
    if (passwordValue === '') {
        errorInput(password, 'A senha é obrigatória')
    } else if (passwordValue.length < 8) {
        errorInput(password, 'A senha deve ter pelo menos 8 caracteres')
    } else {
        const formItem = password.parentElement;
        formItem.className = 'form-content'
    }
}

function checkInputPasswordConfirmation() {
    const passwordValue = password.value;
    const confirmationPasswordValue = passwordConfirmation.value;
    if (confirmationPasswordValue === '') {
        errorInput(passwordConfirmation, 'confirmação obrigatória')
    } else if (confirmationPasswordValue !== passwordValue) {
        errorInput(passwordConfirmation, 'As senhas não conferem')
    } else {
        const formItem = passwordConfirmation.parentElement;
        formItem.className = 'form-content'
    }
}


function checkForm () {
    checkInputUsername();
    checkInputEmail();
    checkInputTelefone();
    checkInputCpf();
    checkInputData();
    checkInputGenero();
    checkInputRua();
    checkInputNumero();
    checkInputBairro();
    checkInputCidade();
    checkInputUf();
    checkInputCep();
    checkInputPassword();
    checkInputPasswordConfirmation();

    const formItems = form.querySelectorAll('.form-content');
    const isValid = [...formItems].every((item) => {
        return item.className === 'form-content'
    });

    if (isValid) {
        alert('Usuário cadastrado com sucesso!');
    }
    else {
        alert('Por favor, verifique os campos obrigatórios.');
    }
}



function errorInput(input, message) {
    const formItem = input.parentElement;
    const textMessage = formItem.querySelector('a')

    textMessage.innerText = message;

    formItem.className = 'form-content error';
}