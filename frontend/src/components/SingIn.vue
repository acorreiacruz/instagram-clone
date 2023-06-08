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
                                    <!-- Name -->
                                    <div class="form-group col-md-12 mb-4">
                                        <input type="text" class="form-control input-lg" aria-describedby="nameHelp"
                                            placeholder="Nome" v-model="username" required />
                                    </div>
                                    <!-- E-mail -->
                                    <div class="form-group col-md-12 mb-4">
                                        <input type="email" class="form-control input-lg" aria-describedby="emailHelp"
                                            placeholder="E-mail" v-model="email" required />
                                    </div>
                                    <!-- Password -->
                                    <div class="form-group col-md-12 mb-4">
                                        <input type="password" class="form-control input-lg" placeholder="Senha"
                                            v-model="password" required />
                                    </div>
                                    <!-- CPassword -->
                                    <div class="form-group col-md-12 mb-4">
                                        <input type="password" class="form-control input-lg" placeholder="Confirme a Senha"
                                            v-model="cpassword" :pattern="`^${password}$`"
                                            title="A confirmação de senha deve ser igual à senha" required />
                                    </div>
                                    <div class="col-md-12">
                                        <div class="d-flex justify-content-center align-items-center">
                                            <button @click="validarCampos" type="submit" class="btn mb-4">Cadastrar</button>
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
export default {
    data() {
        return {
            username: "",
            fullname: "",
            email: "",
            password: "",
            cpassword: "",
        };
    },
    methods: {
        submitForm() {
            fetch("/api/register/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    username: this.username,
                    fullname: this.fullname,
                    email: this.email,
                    password: this.password,
                    cpassword: this.cpassword,
                }),
            })
                .then((response) => response.json())
                .then((data) => {
                    console.log(data);
                    // Aqui você pode realizar as ações necessárias após o cadastro
                })
                .catch((error) => {
                    console.error(error);
                });
        },
    },
};
</script>
  
<style scoped>
@import "@/assets/css/style.css";
</style>