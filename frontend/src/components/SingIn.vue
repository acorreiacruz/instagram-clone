<template>
    <div class="container d-flex align-items-center justify-content-center" style="min-height: 100vh">
        <div class="d-flex flex-column justify-content-between">
            <div class="row justify-content-center">
                <div class="col-lg-6 col-xl-5 col-md-10">
                    <div class="card card-default card-gradient mb-0">
                        <div class="card-header pb-0">
                            <div class="app-brand w-100 d-flex justify-content-center border-bottom-0">
                                <a class="w-auto pl-0">
                                    <div class="d-flex flex-column align-items-center">
                                        <img src="@/assets/images/logo.png" alt="logo" />
                                        <span class="logo-name text-dark">Micro-Instagram</span>
                                    </div>
                                </a>
                            </div>
                        </div>

                        <div class="card-body px-5 pb-5 pt-0">
                            <form @submit.prevent="submitForm">
                                <div class="row">
                                    <!-- Username -->
                                    <div class="form-group col-md-12 mb-4">
                                        <input type="text" class="form-control input-lg" placeholder="Usuario"
                                            v-model="username" required>
                                    </div>
                                    <!-- Name -->
                                    <div class="form-group col-md-12 mb-4">
                                        <input type="text" class="form-control input-lg" placeholder="Nome Completo"
                                            v-model="name" required />
                                    </div>
                                    <!-- E-mail -->
                                    <div class="form-group col-md-12 mb-4">
                                        <input type="email" class="form-control input-lg" placeholder="E-mail"
                                            v-model="email" required />
                                    </div>
                                    <!-- Password -->
                                    <div class="form-group col-md-12 mb-4">
                                        <input type="password" class="form-control input-lg" placeholder="Senha"
                                            v-model="password" required />
                                    </div>
                                    <div class="col-md-12">
                                        <div class="d-flex justify-content-center align-items-center">
                                            <button type="submit" class="btn mb-4">Cadastrar</button>
                                        </div>
                                    </div>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
  
<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      name: '',
      email: '',
      password: ''
    };
  },
  methods: {
    submitForm() {
      const formData = {
        username: this.username,
        name: this.name,
        email: this.email,
        password: this.password
      };

      axios.post('/api/records/', formData)
        .then(response => {
          console.log('Sucesso!', response.data);
          // Aqui você pode adicionar código para redirecionar para outra página ou exibir uma mensagem de sucesso
        })
        .catch(error => {
          console.error('Erro:', error.response.data);
          // Aqui você pode adicionar código para exibir uma mensagem de erro ao usuário
        });
    }
  }
};
</script>

<style>
@import '~bootstrap/dist/css/bootstrap.css';
</style>
