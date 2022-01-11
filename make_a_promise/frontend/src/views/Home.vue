<template>
  <div class="main-section">
    <Form @closeForm="handleCloseForm" v-show="showModal" class="modal" />
    <div class="card-component" v-if="allPromises">
      <Card :allPromises="allPromises" @openModal="handleOpenModal" />
    </div>
  </div>
</template>

<script>
import Card from '../components/Card';
import Form from '../components/Form';
import axios from 'axios';
export default {
  components: { Card, Form },
  created() {
    this.getData();
  },
  mounted() {},
  data() {
    return {
      url: 'api/v1/promise-api/',
      allPromises: [],
      title: '',
      text: '',
      name: '',
      color: '#e66465',
      showModal: false,
    };
  },

  methods: {
    handleCloseForm() {
      this.showModal = !this.showModal;
      document.body.style.overflow = 'hidden scroll';
    },
    handleOpenModal() {
      this.showModal = !this.showModal;
      document.body.style.overflow = 'hidden';
    },
    // getData
    async getData() {
      try {
        let response = await axios.get(this.url);
        this.allPromises = await response.data.results;
        this.next = await response.data.next;
      } catch (err) {
        console.log(`ERROR: ${err}`);
      }
    },
    async send_promise_made() {
      // if (this.title.length && this.text.length) {
      let data = {
        title: this.title,
        text: this.text,
        name: this.name,
        color: this.color,
      };
      try {
        axios.post(this.url, data);
        this.title = '';
        this.text = '';
      } catch (err) {
        console.log(`ERROR: ${err}`);
      }
      // this.showContainer = false;
      // }
    },
  },
};
</script>

<style scoped>
.main-section {
  height: 100%;
  width: 100%;
  /* max-width: 90vw; */
}
.modal-open {
  overflow: hidden;
  display: none;
}
.modal {
  position: fixed;
  height: 100%;
  width: 100vw;
  z-index: 2;
  top: 0;
  left: 0;
}
</style>
