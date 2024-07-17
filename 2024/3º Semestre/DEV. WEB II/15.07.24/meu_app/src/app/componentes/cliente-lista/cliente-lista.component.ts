import { Component, OnInit } from '@angular/core';
import { Cliente } from '../model/cliente';

@Component({
  selector: 'app-cliente-lista',
  templateUrl: './cliente-lista.component.html',
  styleUrl: './cliente-lista.component.css'
})
export class ClienteListaComponent implements OnInit {
  clienteLista: Cliente[] = [];
  cliente1: Cliente = new Cliente();
  cliente2: Cliente = new Cliente();

  ngOnInit(): void {
    this.cliente1.id = 1;
    this.cliente1.nome = 'João';
    this.cliente1.id_cidade_lookup = 1;
    this.clienteLista.push(this.cliente1);

    this.cliente2.id = 2;
    this.cliente2.nome = 'Pedro';
    this.cliente2.id_cidade_lookup = 1;
    this.clienteLista.push(this.cliente2);
  }
}
