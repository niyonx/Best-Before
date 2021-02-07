<template>
    <div>
        <base-header type="gradient-success" class="pb-6 pb-8 pt-5 pt-md-8">
            <!-- Card stats -->
            <div class="row">
                <div class="col-xl-3 col-lg-6">
                    <stats-card title="Total Articles"
                                type="gradient-info"
                                sub-title="350,897"
                                icon="fa fa-history"
                                class="mb-4 mb-xl-0"
                    >
                    </stats-card>
                </div>
                <div class="col-xl-3 col-lg-6">
                    <stats-card title="Total Expired"
                                type="gradient-danger"
                                sub-title="2,356"
                                icon="fa fa-ban"
                                class="mb-4 mb-xl-0"
                    >
                    </stats-card>
                </div>
                <div class="col-xl-3 col-lg-6">
                    <stats-card title="Total Warnings"
                                type="gradient-warning"
                                sub-title="924"
                                icon="fa fa-exclamation"
                                class="mb-4 mb-xl-0"
                    >
                    </stats-card>

                </div>
                <div class="col-xl-3 col-lg-6">
                    <stats-card title="Total Safe"
                                type="gradient-green"
                                sub-title="49,65%"
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
                            <ProjectsTable></ProjectsTable>
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

// Tables
import ProjectsTable from './Tables/ProjectsTable'

export default {
  components: {
    MyArticles,
    ProjectsTable
  }
}
</script>
<style></style>
