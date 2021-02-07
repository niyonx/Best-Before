<template>
        <div class="row justify-content-center">
            <div class="col-lg-5 col-md-7">
                <div class="card bg-secondary shadow border-0">
                    <div class="card-body px-lg-5 py-lg-5">
                        <div class="text-center text-muted mb-4">
                            <p class="display-4"><a id="target"></a>Sign in with credentials</p>
                            <!-- <small>{{this.error}}</small> -->
                        </div>
                        <div v-if='this.error'>
                            <div role="alert" class="alert alert-warning"><strong>Aye!</strong>
                            {{this.error}}
                              </div>
                        </div>
                        <form role="form">
                            <base-input class="input-group-alternative mb-3"
                                        placeholder="Username"
                                        addon-left-icon="fa fa-user"
                                        v-model="model.username">
                            </base-input>

                            <base-input class="input-group-alternative"
                                        placeholder="Password"
                                        type="password"
                                        addon-left-icon="ni ni-lock-circle-open"
                                        v-model="model.password">
                            </base-input>
<!--                            <base-checkbox class="custom-control-alternative">-->
<!--                                <span class="text-muted">Remember me</span>-->
<!--                            </base-checkbox>-->
                            <div class="text-center">
                                <base-button type="primary" class="my-4" @click="checkUser(model.username, model.password)">Sign in</base-button>
                            </div>
                        </form>
                    </div>
                </div>
                <div class="row mt-3">
                    <div class="col-6">
<!--                        <a href="#" class="text-light"><small>Forgot password?</small></a>-->
                    </div>
                    <div class="col-6 text-right">
                        <router-link to="/register" class="text-light"><small>Create new account</small></router-link>
                    </div>
                </div>
            </div>
        </div>
</template>
<script>

import $backend from '../backend'

export default {
  name: 'login',
  data () {
    return {
      model: {
        username: '',
        password: ''
      },
      error: ''
    }
  },
  methods: {
    checkUser (username, password) {
      $backend.checkUser(username, password)
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
