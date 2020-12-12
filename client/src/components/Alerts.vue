<template>
  <div>
    <table>
      <thead>
        <tr>
          <th>Message Id</th>
          <th>KPI Threshold</th>
          <th>KPI Value</th>
          <th>Line</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(alert, index) in alerts" :key="index">
          <td>{{ alert.messageId }}</td>
          <td>{{ alert.KPIThreshold }}</td>
          <td>{{ alert.KPIValue }}</td>
          <td>{{ alert.line }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Alerts',
  data() {
    return {
      alerts: [],
    };
  },
  methods: {
    getAlerts() {
      const path = 'http://localhost:8000/alerts';
      axios.get(path)
        .then((res) => {
          this.alerts = res.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  created() {
    this.getAlerts();
  },
};
</script>
