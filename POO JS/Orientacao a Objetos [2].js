
// Classe
function Pessoa(nome, ida) {                         // CLASSE PAI
    this.nome = nome;
    this.idade = ida;
}
Pessoa.prototype.retornarDados = function() {
    return `Nome: ${this.nome}, idade: ${this.idade}, Tipo: ${this.tipo}, Documento: ${this.cpf}`
}

function PessoaFisica(nome, ida, cpf) {              // CLASSE FILHA
    Pessoa.call(this, nome, ida)
    this.cpf = cpf;
    this.tipo = 'Fisica';
} 

PessoaFisica.prototype = Pessoa.prototype;

// Objetos
var pessoa1 = new PessoaFisica('Joao', 25, '141656424')
var pessoa2 = new Pessoa('Tetulho', 55)

// -----------------------------------------------------------------------

console.log(`Pessoa 1 = ${pessoa1.retornarDados()}`)
console.log(`Pessoa 2 = ${pessoa2.retornarDados()}`)
