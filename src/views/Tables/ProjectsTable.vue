<template>
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
</template>
<script>
import $backend from '../../backend'

export default {
  name: 'projects-table',
  props: {
    type: {
      type: String
    },
    name: String
  },
  data () {
    return {
      tableData: []
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
      console.log(currentDate)
      // var currentDateWithFormat = new Date().toJSON().slice(0, 10).replace(/-/g, '/')
      var difference = Math.floor((expiryDate - currentDate) / (1000 * 60 * 60 * 24))

      if (difference <= 0) { return 'Expired' } else if (difference <= 7) { return 'Warning' } else { return 'Safe' }
    },
    getExpiryStatusType (expiryDate) {
      var currentDate = new Date()
      var expiryDate = new Date(expiryDate)
      console.log(currentDate)
      // var currentDateWithFormat = new Date().toJSON().slice(0, 10).replace(/-/g, '/')
      var difference = Math.floor((expiryDate - currentDate) / (1000 * 60 * 60 * 24))

      if (difference <= 0) { return 'danger' } else if (difference <= 7) { return 'warning' } else { return 'success' }
    }
  },
  beforeMount () {
    this.getProducts()
  }
}
</script>
<style>
</style>
