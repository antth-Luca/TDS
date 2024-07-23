import { Component } from '@angular/core';
import { Cidade } from '../model/cidade';
import { CidadeService } from '../../services/cidade.service';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-cidade-form',
  templateUrl: './cidade-form.component.html',
  styleUrl: './cidade-form.component.css'
})
export class CidadeFormComponent {
  constructor(private service: CidadeService, private router: Router, private activateRout: ActivatedRoute) { }

  ngOnInit(): void {
    const id = this.activateRout.snapshot.paramMap.get('id');
    if (id) {
      // TODO: Preencher aqui!
    }
  };

  cidade: Cidade = new Cidade();

  salvar() {
    this.service.salvar(this.cidade);
  };
}
