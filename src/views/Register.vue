<template>
    <div class="row justify-content-center">
        <div class="col-lg-5 col-md-7">
            <div class="card bg-secondary shadow border-0">

                <div class="card-body px-lg-5 py-lg-5">
                    <div class="text-center text-muted mb-4">
                        <p class="display-4">Sign up with credentials</p>
                    </div>
                    <form role="form">
                        <base-input class="input-group-alternative mb-3"
                                    placeholder="Username"
                                    addon-left-icon="fa fa-user"
                                    v-model="model.username"
                                    >
                        </base-input>

                        <!-- <base-input class="input-group-alternative mb-3"
                                    placeholder="Email"
                                    addon-left-icon="ni ni-email-83"
                                    v-model="model.email">
                        </base-input> -->

                        <base-input class="input-group-alternative"
                                    placeholder="Password"
                                    type="password"
                                    addon-left-icon="ni ni-lock-circle-open"
                                    v-model="model.password">
                        </base-input>

                         <base-input class="input-group-alternative"
                                    placeholder="Email"
                                    type="text"
                                    addon-left-icon="fa fa-envelope"
                                    v-model="model.phone">
                        </base-input>
                        <div class="text-center">
                            <base-button type="primary" class="my-4"
                                    @click="createUser(model.username, model.password, model.phone)"

                            >Create account</base-button>
                        </div>
                    </form>
                </div>
            </div>
            <div class="row mt-3">
                <div class="col-6">
                </div>
                <div class="col-6 text-right">
                    <router-link to="/login" class="text-light">
                        <small>Login into your account</small>
                    </router-link>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import $backend from '../backend'

export default {
  name: 'register',
  data () {
    return {
      model: {
        username: '',
        phone: '',
        password: ''
      },
      error: ''
    }
  },
  methods: {
    createUser (username, password, phone) {
      $backend.createUser(username, password, phone)
        .then(responseData => {
          if (responseData == true) {
            this.$router.push('dashboard')
          } else {
            this.error = 'Invalid username or password!'
          }
        }).catch(error => {
          this.error = error.message
        })
    }
  }
}
</script>
<style>
</style>
