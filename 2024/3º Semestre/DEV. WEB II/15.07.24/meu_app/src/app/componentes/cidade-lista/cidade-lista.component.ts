import { Component, OnInit } from '@angular/core';
import { Cidade } from '../model/cidade';

@Component({
  selector: 'app-cidade-lista',
  templateUrl: './cidade-lista.component.html',
  styleUrl: './cidade-lista.component.css'
})
export class CidadeListaComponent implements OnInit {
  cidadeLista: Cidade[] = [];
  cidade1: Cidade = new Cidade();
  cidade2: Cidade = new Cidade();

  ngOnInit(): void {
    this.cidade1.id = 1;
    this.cidade1.nome = 'Astorga';
    this.cidade1.uf = 'PR';
    this.cidadeLista.push(this.cidade1);

    this.cidade2.id = 2;
    this.cidade2.nome = 'Maringá';
    this.cidade2.uf = 'PR';
    this.cidadeLista.push(this.cidade2);
  }
}
