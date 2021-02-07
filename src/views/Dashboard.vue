<template>
    <div>
        <base-header type="gradient-success" class="pb-6 pb-8 pt-5 pt-md-8">
            <!-- Card stats -->
            <div class="row">
                <div class="col-xl-3 col-lg-6">
                    <stats-card title="Total Articles"
                                type="gradient-info"
                                :sub-title="total"
                                icon="fa fa-history"
                                class="mb-4 mb-xl-0"
                    >
                    </stats-card>
                    <!-- {{total}} -->
                </div>
                <div class="col-xl-3 col-lg-6">
                    <stats-card title="Total Expired"
                                type="gradient-danger"
                                :sub-title="8"
                                icon="fa fa-ban"
                                class="mb-4 mb-xl-0"
                    >
                    </stats-card>
                     <!-- {{totalWarn}} -->
                </div>
                <div class="col-xl-3 col-lg-6">
                    <stats-card title="Total Warnings"
                                type="gradient-warning"
                                :sub-title="6"
                                icon="fa fa-exclamation"
                                class="mb-4 mb-xl-0"
                    >
                    </stats-card>

                </div>
                <div class="col-xl-3 col-lg-6">
                    <stats-card title="Total Safe"
                                type="gradient-green"
                                :sub-title="5"
                                icon="fa fa-smile"
                                class="mb-4 mb-xl-0"
                    >
                    </stats-card>
                </div>
            </div>
        </base-header>
        <div class="container-fluid mt--7">
            <div class="row">
                <div class="col">
                    <div class="card shadow">
                        <div class="card-header bg-transparent">
                            <div class="card shadow"
       :class="type === 'dark' ? 'bg-default': ''">
    <div class="card-header border-0"
         :class="type === 'dark' ? 'bg-transparent': ''">
      <div class="row align-items-center">
        <div class="col">
          <h3 class="mb-0" :class="type === 'dark' ? 'text-white': ''">
            My Articles
          </h3>
        </div>
      </div>
    </div>

    <div class="table-responsive">
      <base-table class="table align-items-center table-flush"
                  :class="type === 'dark' ? 'table-dark': ''"
                  :thead-classes="type === 'dark' ? 'thead-dark': 'thead-light'"
                  tbody-classes="list"
                  :data="tableData">
        <template slot="columns">
          <th>Article Name</th>
          <th>Article Brand</th>
          <th>Expiry Date</th>
          <th>Status</th>
          <th></th>
        </template>

        <template slot-scope="{row}">
          <th scope="row">
            <div class="media align-items-center">
              <div class="media-body">
                <span class="name mb-0 text-sm">{{row.product_name}}</span>
              </div>
            </div>
          </th>
          <td>
            {{row.product_brand}}
          </td>
          <td>
           {{row.expiry_date}}
          </td>
           <td>
             <!-- success, warning, danger --- safe, expired, warning -->
            <badge pill :type="getExpiryStatusType(row.expiry_date)">{{getExpiryStatus(row.expiry_date)}}</badge>
          </td>

          <td class="text-right">
               <base-button  @click="deleteProduct(row.product_id)" type="secondary" icon="fa fa-trash"></base-button>
          </td>

        </template>
      </base-table>
    </div>

  </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
// My articles
import MyArticles from './MyArticles'
import $backend from '../backend'
// Tables
import ProjectsTable from './Tables/ProjectsTable'

export default {
    components: {
        MyArticles,
    ProjectsTable
    },
    props: {
    type: {
      type: String
    },
    name: String,
    total: 0,
  },
  data : {
      total: 0,
    totalExp: 'sss',

      totalWarn: 0,
      totalSafe: 0
  },
  data () {
    return {
      tableData: [],
      
    }
  },
  methods: {
    deleteProduct (product_id) {
      $backend.deleteProduct(product_id)
        .then(responseData => {
          console.log('success!')
          this.$router.push('dashboard')
        }).catch(error => {
          this.error = error.message
        })
    },
    getProducts () {
      $backend.getProducts()
        .then(responseData => {
          this.tableData = responseData
        }).catch(error => {
          this.error = error.message
        })
    },
    getExpiryStatus (expiryDate) {
      var currentDate = new Date()
      var expiryDate = new Date(expiryDate)
    //   console.log(currentDate)
      // var currentDateWithFormat = new Date().toJSON().slice(0, 10).replace(/-/g, '/')
      var difference = Math.floor((expiryDate - currentDate) / (1000 * 60 * 60 * 24))

      if (difference <= 0) { 
        //   this.totalExp = parseInt(this.totalExp) + parseInt(1)
          return 'Expired'

           } else if (difference <= 7) {
            //    this.totalWarn = parseInt(this.totalWarn) + parseInt(1)
                return 'Warning' } else { 
                    // this.totalSafe = parseInt(this.totalSafe) + parseInt(1)
                    return 'Safe' }
    },
    getExpiryStatusType (expiryDate) {
      var currentDate = new Date()
      var expiryDate = new Date(expiryDate)
    //   console.log(currentDate)
      // var currentDateWithFormat = new Date().toJSON().slice(0, 10).replace(/-/g, '/')
      var difference = Math.floor((expiryDate - currentDate) / (1000 * 60 * 60 * 24))

      if (difference <= 0) { 
        //   this.totalExp = parseInt(this.totalExp) + parseInt(1)
      return 'danger' } else if (difference <= 7) { 
        //   this.totalWarn = parseInt(this.totalWarn) + parseInt(1)
          return 'warning' } else { 
            //   this.totalSafe = parseInt(this.totalSafe) + parseInt(1)
              return 'success' }
    },
    totalProducts () {
          $backend.totalProducts()
        .then(responseData => {
          this.total = responseData
        }).catch(error => {
          this.error = error.message
        })
      }
  },
  beforeMount () {
    this.getProducts()
    this.totalProducts()
  }
}
</script>
<style></style>
