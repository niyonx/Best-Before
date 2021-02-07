<template>
  <div class="card shadow"
       :class="type === 'dark' ? 'bg-default': ''">
    <div class="card-header border-0"
         :class="type === 'dark' ? 'bg-transparent': ''">
      <div class="row align-items-center">
        <div class="col">
          <h3 class="mb-0" :class="type === 'dark' ? 'text-white': ''">
            {{name}}
          </h3>
        </div>
        <div class="col text-right">
          <base-button type="primary" size="sm">See all</base-button>
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
                <span class="name mb-0 text-sm">{{row.name}}</span>
              </div>
            </div>
          </th>
          <td>
            {{row.brand}}
          </td>
          <td>
           {{row.expiry}}
          </td>
           <td>
            <badge pill :type="row.statusType">{{row.status}}</badge>
          </td>

          <td class="text-right">
               <base-button  type="secondary" icon="fa fa-trash"></base-button>
          </td>

        </template>

      </base-table>
    </div>

    <div class="card-footer d-flex justify-content-end"
         :class="type === 'dark' ? 'bg-transparent': ''">
      <base-pagination total="30"></base-pagination>
    </div>

  </div>
</template>
<script>
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
      tableData: [
        {
          name: 'Argon Design System',
          brand: '$2500 USD',
          status: 'warning',
          statusType: 'warning',
          expiry: '01-01-2002'
        },
        {
          name: 'Angular Now UI Kit PRO',
          brand: '$1800 USD',
          status: 'safe',
          statusType: 'success',
          expiry: '10-12-2020'
        },
        {
          name: 'Black Dashboard',
          brand: '$3150 USD',
          status: 'expired',
          statusType: 'danger',
          expiry: '12-12-1999'
        },
        {
          name: 'React Material Dashboard',
          brand: '$4400 USD',
          status: 'safe',
          statusType: 'success',
          expiry: '09-13-2020'
        },
        {
          name: 'Vue Paper UI Kit PRO',
          brand: '$2200 USD',
          status: 'safe',
          statusType: 'success',
          expiry: '12-12-2013'
        }
      ]
    }
  }
}
</script>
<style>
</style>
