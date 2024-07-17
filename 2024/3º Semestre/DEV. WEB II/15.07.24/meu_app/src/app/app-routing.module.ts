import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './componentes/home/home.component';
import { CidadeFormComponent } from './componentes/cidade-form/cidade-form.component';
import { CidadeListaComponent } from './componentes/cidade-lista/cidade-lista.component';
import { ClienteFormComponent } from './componentes/cliente-form/cliente-form.component';
import { ClienteListaComponent } from './componentes/cliente-lista/cliente-lista.component';

const routes: Routes = [
  {path: '', redirectTo: '/home', pathMatch: 'full'},
  {path: 'home', component: HomeComponent},
  {path: 'cidade-form', component: CidadeFormComponent},
  {path: 'cidade-lista', component: CidadeListaComponent},
  {path: 'cliente-form', component: ClienteFormComponent},
  {path: 'cliente-lista', component: ClienteListaComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
