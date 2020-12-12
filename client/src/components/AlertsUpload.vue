<template>
  <div class="container">
    <div class="large-12 medium-12 small-12 cell">
      <label>Files
        <input type="file" id="files" ref="files" multiple v-on:change="handleFilesUpload()"/>
      </label>
      <button v-on:click="submitFiles()">Submit</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  /*
      Defines the data used by the component
    */
  data() {
    return {
      files: '',
    };
  },

  methods: {
    /*
        Submits all of the files to the server
      */
    submitFiles() {
      /*
          Initialize the form data
        */
      // const formData = new FormData();

      /*
          Iteate over any file sent over appending the files
          to the form data.
        */
      for (let i = 0; i < this.files.length; i += 1) {
        const formData = new FormData();
        formData.append('file', this.files[i]);
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
      }

      /*
          Make the request to the POST /multiple-files URL
        */
      // axios.post('http://localhost:8000/alerts/uploadfile',
      //   formData,
      //   {
      //     headers: {
      //       'Content-Type': 'multipart/form-data',
      //     },
      //   }).then(() => {
      //   console.log('SUCCESS!!');
      // })
      //   .catch(() => {
      //     console.log('FAILURE!!');
      //   });
    },

    /*
        Handles a change on the file upload
      */
    handleFilesUpload() {
      this.files = this.$refs.files.files;
    },
  },
};
</script>
