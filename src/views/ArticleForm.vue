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
                                    <base-button type="primary" size="sm" icon="fa fa-plus">Add</base-button>
                                </div>
                            </div>
                        </div>
                        <template>
                            <form @submit.prevent>
                                <h6 class="heading-small text-muted mb-4">Article information</h6>
                                <div class="pl-lg-4">
                                    <div class="row">
                                        <div class="col-lg-6">
                                            <base-input alternative=""
                                                        label="Article name"
                                                        placeholder="Article name"
                                                        input-classes="form-control-alternative"
                                                        :value="nameLoaded"
                                            />
                                        </div>
                                        <div class="col-lg-6">
                                            <base-input alternative=""
                                                        label="Article Brand"
                                                        placeholder="Article Brand"
                                                        input-classes="form-control-alternative"
                                                        :value="brandLoaded"
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
                                            />
                                        </div>
                                        <div class="col-lg-3">
                                            <p class="form-control-label">Date</p>
                                            <base-button :loading="isExpirySelecting" @click="onExpiryButtonClick" type="primary"
                                                         size="sm" :icon="expiryIcon">{{expiryButtonText}}
                                            </base-button>
                                            <input ref="expiry"
                                                   class="d-none"
                                                   type="file"
                                                   accept="image/*"
                                                   @change="onExpiryFileChanged">
                                        </div>
                                        <div class="col-lg-3">
                                            <p class="form-control-label">Barcode</p>
                                            <base-button :loading="isBarcodeSelecting" @click="onBarcodeButtonClick" type="primary"
                                                         size="sm" :icon="barcodeIcon"> {{barcodeButtonText}}
                                            </base-button>
                                            <input ref="barcode"
                                                   class="d-none"
                                                   type="file"
                                                   accept="image/*"
                                                   @change="onBarcodeFileChanged">
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
import axios from 'axios'
export default {
  name: 'user-profile',
  data () {
    return {
      defaultButtonText: 'Upload',
      defaultIcon: 'fa fa-upload',
      uploadedIcon: 'ni ni-image',
      selectedExpiryFile: null,
      selectedBarcodeFile: null,
      isExpirySelecting: false,
      isBarcodeSelecting: false,
      articleName: '',
      articleBrand: '',
      expiryDate: '',
      error: '',
      barcodeLoading: false,
      expiryLoading: false
    }
  },
  computed: {
    expiryButtonText () {
      return this.selectedExpiryFile ? this.selectedExpiryFile.name : this.defaultButtonText
    },
    barcodeButtonText () {
      return this.selectedBarcodeFile ? this.selectedBarcodeFile.name : this.defaultButtonText
    },
    expiryIcon () {
      return this.selectedExpiryFile ? this.uploadedIcon : this.defaultIcon
    },
    barcodeIcon () {
      return this.selectedBarcodeFile ? this.uploadedIcon : this.defaultIcon
    },
    nameLoaded () {
      return this.barcodeLoading ? this.articleName : ''
    },
    brandLoaded () {
      return this.barcodeLoading ? this.articleBrand : ''
    }
  },
  methods: {
    onExpiryButtonClick () {
      this.isExpirySelecting = true
      window.addEventListener('focus', () => {
        this.isExpirySelecting = false
      }, { once: true })

      this.$refs.expiry.click()
    },
    onBarcodeButtonClick () {
      this.isBarcodeSelecting = true
      window.addEventListener('focus', () => {
        this.isBarcodeSelecting = false
      }, { once: true })

      this.$refs.barcode.click()
    },
    async onExpiryFileChanged (e) {
      this.selectedExpiryFile = e.target.files[0]
      let formData = new FormData()
      formData.append('file', this.selectedExpiryFile)
      // Calling expiry api
      await axios
        .post('api/uploadExpiry', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        })
        .then((response) => {
          this.expiryLoading = true
          const data = response.data
          console.log(data)
        })
        .catch(function (error) {
          if (error.response) {
            this.error = error.response.data
          } else { this.error = 'uh oh, an error happened...' }
          this.barcodeLoading = false
        })
    }
  },
  async onBarcodeFileChanged (e) {
    this.selectedBarcodeFile = e.target.files[0]
    let formData = new FormData()
    formData.append('file', this.selectedBarcodeFile)
    // Calling barcode api
    await axios
      .post('api/uploadBarcode', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })
      .then((response) => {
        this.barcodeLoading = true
        const data = response.data
        this.articleName = data.product_name
        this.articleBrand = data.brand
      })
      .catch(function (error) {
        if (error.response) {
          this.error = error.response.data
        } else { this.error = 'uh oh, an error happened...' }
        this.barcodeLoading = false
      })
  }
}
</script>
<style></style>
