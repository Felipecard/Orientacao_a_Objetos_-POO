
// MOLDE
class Cliente {
    nome;
    cpf;

}

class ContaCorrente {
    agencia;
    // #saldo = 0; Ainda nao esta implementada.. mas realmente tornaria privada.. Hoje a convencao é usar _saldo
    _saldo = 0;

    sacar(valor) {
        if(this._saldo >= valor) {
            this._saldo -= valor;
            return valor;
        }
    }

    depositar(valor) {
        if(valor <= 0) {
            return;             // URLY RETURN
        }

        this._saldo += valor;
    }
}


const cliente1 = new Cliente();    // OBJETO
cliente1.nome = 'Ricardo';
cliente1.cpf = '141565478';

const cliente2 = new Cliente();     // OBJETO
cliente2.nome = 'Alice';
cliente2.cpf = '33354865';


const contaCorrenteRicardo = new ContaCorrente();       // OBJETO

contaCorrenteRicardo.agencia = 1001;

contaCorrenteRicardo.depositar(100);


const valorSacado = contaCorrenteRicardo.sacar(40)

console.log(valorSacado);
console.log(contaCorrenteRicardo); 



