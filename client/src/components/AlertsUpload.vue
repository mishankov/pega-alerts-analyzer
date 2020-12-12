<template>
  <div class="container">
    <div class="large-12 medium-12 small-12 cell">
      <label>File
        <input type="file" id="file" ref="file" v-on:change="handleFileUpload()"/>
      </label>
      <button v-on:click="submitFile()">Submit</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
/*
    Defines the data used by the component
*/
  name: 'AlertsUpload',
  data() {
    return {
      file: '',
    };
  },

  methods: {
    /*
    Submits the file to the server
    */
    submitFile() {
    /*
            Initialize the form data
        */
      const formData = new FormData();

      /*
            Add the form data we need to submit
        */
      formData.append('file', this.file);

      /*
        Make the request to the POST /single-file URL
    */
      axios.post('http://localhost:8000/alerts/uploadfile',
        formData,
        {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        }).then(() => {
        console.log('SUCCESS!!');
      })
        .catch(() => {
          console.log('FAILURE!!');
        });
    },

    /*
    Handles a change on the file upload
    */
    handleFileUpload() {
      const index = 0;
      this.file = this.$refs.file.files[index];
    },
  },
};
</script>
