import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './componentes/home/home.component';
import { CidadeFormComponent } from './componentes/cidade-form/cidade-form.component';
import { CidadeListaComponent } from './componentes/cidade-lista/cidade-lista.component';
import { ClienteFormComponent } from './componentes/cliente-form/cliente-form.component';
import { ClienteListaComponent } from './componentes/cliente-lista/cliente-lista.component';

const routes: Routes = [
  // Padrão
  {path: '', redirectTo: '/home', pathMatch: 'full'},
  // Geral
  {path: 'home', component: HomeComponent},
  // Cidade
  {path: 'cidade-form', component: CidadeFormComponent},
  {path: 'cidade-form/:id', component: CidadeFormComponent},
  {path: 'cidade-lista', component: CidadeListaComponent},
  // Cliente
  {path: 'cliente-form', component: ClienteFormComponent},
  {path: 'cliente-form/:id', component: ClienteFormComponent},
  {path: 'cliente-lista', component: ClienteListaComponent},

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
