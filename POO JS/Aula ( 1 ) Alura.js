
// MOLDE
class Cliente {
    nome;
    cpf;

}

class ContaCorrente {
    agencia;
    saldo;

    sacar(valor) {
        if(this.saldo >= valor) {
            this.saldo -= valor;
        }
    }

    depositar(valor) {
        if(valor > 0) {
            this.saldo += valor;
        }
    }
}


const cliente1 = new Cliente();    // OBJETO
cliente1.nome = 'Ricardo';
cliente1.cpf = '141565478';

const cliente2 = new Cliente();     // OBJETO
cliente2.nome = 'Alice';
cliente2.cpf = '33354865';


const contaCorrenteRicardo = new ContaCorrente();       // OBJETO
contaCorrenteRicardo.saldo = 0;
contaCorrenteRicardo.agencia = 1001;
console.log(contaCorrenteRicardo.saldo); //print 1
contaCorrenteRicardo.depositar(100);
console.log(contaCorrenteRicardo.saldo); //print 2

contaCorrenteRicardo.sacar(70)
console.log(contaCorrenteRicardo.saldo); //print 3




// IMPRIMIR:
console.log(cliente1);
console.log(cliente2);




