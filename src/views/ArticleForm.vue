<template>
    <div>
        <base-header class="header pb-8 pt-5 pt-lg-8 d-flex align-items-center"
                     style="min-height: 600px; background-image: url(img/theme/profile-cover.jpg); background-size: cover; background-position: center top;">
            <!-- Mask -->
            <span class="mask bg-gradient-success opacity-8"></span>
            <!-- Header container -->
            <div class="container-fluid d-flex align-items-center">
                <div class="row">
                    <div class="col-lg-7 col-md-10">
                        <h1 class="display-2 text-white">Add an article</h1>
                        <p class="text-white mt-0 mb-5">This is your profile page. You can see the progress you've made
                            with your work and manage your projects or assigned tasks</p>
                    </div>
                </div>
            </div>
        </base-header>

        <div class="container-fluid mt--7">
            <div class="row">

                <div class="col-xl-12 order-xl-1">
                    <card shadow type="secondary">
                        <div slot="header" class="bg-white border-0">
                            <div class="row align-items-center">
                                <div class="col-8">
                                    <h3 class="mb-0">My article</h3>
                                </div>
                                <div class="col-4 text-right">
                                    <base-button type="primary" size="sm" icon="ni ni-fat-add">Add</base-button>
                                </div>
                            </div>
                        </div>
                        <template>
                            <form @submit.prevent>
                                <h6 class="heading-small text-muted mb-4">Product information</h6>
                                <div class="pl-lg-4">
                                    <div class="row">
                                        <div class="col-lg-6">
                                            <base-input alternative=""
                                                        label="Product name"
                                                        placeholder="Product name"
                                                        input-classes="form-control-alternative"
                                                        v-model="model.name"
                                            />
                                        </div>
                                        <div class="col-lg-6">
                                            <base-input alternative=""
                                                        label="Product Brand"
                                                        placeholder="Product Brand"
                                                        input-classes="form-control-alternative"
                                                        v-model="model.brand"
                                            />
                                        </div>
                                    </div>
                                </div>
                                <div class="pl-lg-4">
                                    <div class="row">
                                        <div class="col-lg-6">
                                            <base-input alternative=""
                                                        label="Expiry Date"
                                                        placeholder="MM-DD-YYYY"
                                                        input-classes="form-control-alternative"
                                                        v-model="model.expiryDate"
                                            />
                                        </div>
                                        <div class="col-lg-3">
                                            <p class="form-control-label">Date</p>
                                            <base-button :loading="isSelecting" @click="onButtonClick" type="primary"
                                                         size="sm" :icon="icon">Upload
                                            </base-button>
                                            <input ref="uploader"
                                                   class="d-none"
                                                   type="file"
                                                   accept="image/*"
                                                   @change="onFileChanged">
                                        </div>
                                        <div class="col-lg-3">
                                            <p class="form-control-label">Barcode</p>
                                            <base-button :loading="isSelecting" @click="onButtonClick" type="primary"
                                                         size="sm" :icon="icon"> {{buttonText}}
                                            </base-button>
                                            <input ref="uploader"
                                                   class="d-none"
                                                   type="file"
                                                   accept="image/*"
                                                   @change="onFileChanged">
                                        </div>
                                    </div>
                                </div>
                            </form>
                        </template>
                    </card>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
export default {
  name: 'user-profile',
  data () {
    return {
      model: {
        name: '',
        brand: '',
        expiryDate: ''
      },
      defaultButtonText: 'Upload',
      defaultIcon: 'ni ni-cloud-upload-96',
      uploadedIcon: 'ni ni-image',
      selectedFile: null,
      isSelecting: false
    }
  },
  computed: {
    buttonText () {
      return this.selectedFile ? this.selectedFile.name : this.defaultButtonText
    },
    icon () {
      return this.selectedFile ? this.uploadedIcon : this.defaultIcon
    }
  },
  methods: {
    onButtonClick () {
      this.isSelecting = true
      window.addEventListener('focus', () => {
        this.isSelecting = false
      }, { once: true })

      this.$refs.uploader.click()
    },
    async onFileChanged (e) {
      this.selectedFile = e.target.files[0]
      // Calling barcode api
    }
  }
}
</script>
<style></style>
