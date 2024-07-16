import { NgModule } from '@angular/core';
import { BrowserModule, provideClientHydration } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './componentes/home/home.component';
import { CidadeListaComponent } from './componentes/cidade-lista/cidade-lista.component';
import { CidadeFormComponent } from './componentes/cidade-form/cidade-form.component';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    CidadeListaComponent,
    CidadeFormComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [
    provideClientHydration()
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
