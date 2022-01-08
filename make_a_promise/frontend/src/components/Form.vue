<template>
  <div class="form-section" @click.self="closeForm">
    <div class="form-container">
      <form class="form" :style="{ background: color, color: fontColor }">
        <div v-show="errors.length" class="errors">
          <!-- errors -->
          <transition name="toast">
            <div v-if="errors.length">
              <div v-for="error in errors" v-bind:key="error" class="toast">
                <p>{{ error }}</p>
              </div>
            </div>
          </transition>
        </div>
        <!-- errors -->
        <div class="title form-input">
          <label>Title</label>
          <input type="text" v-model="title" maxlength="40" />
        </div>
        <div class="underline"></div>
        <div class="options">
          <div class="color">
            <label>Card Color</label>
            <input type="color" v-model="color" />
          </div>
          <div class="color">
            <label>Font Color</label>
            <input type="color" v-model="fontColor" />
          </div>
        </div>

        <div class="name form-input">
          <label>Name</label>
          <input type="text" v-model="name" />
        </div>
        <div class="text form-input">
          <textarea placeholder="I promise..." v-model="text"></textarea>
          <div v-if="this.text.length > 200">
            <p>{{ CharactersRemaining }}</p>
          </div>
        </div>
        <button
          class="btn"
          @click.prevent="send_promise_made"
          :style="{ background: fontColor }"
        >
          SEND
        </button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      url: 'api/v1/promise-api/',
      title: '',
      text: '',
      name: '',
      color: '#e66465',
      fontColor: '#ffffff',
      errors: [],
    };
  },
  computed: {
    CharactersRemaining() {
      if (this.text.length >= 0) {
        return `Characters remaining ${300 - this.text.length}`;
      } else if (this.text.length > 300) {
        return `Characters exceeded ${this.text.length - 300}`;
      }
      return true;
    },
  },
  methods: {
    closeForm() {
      this.$emit('closeForm');
    },
    async send_promise_made() {
      // title error
      if (this.title === '' || this.name === '' || this.text === '') {
        this.errors.push('Please, complete all the fields');
        setTimeout(() => {
          this.errors = [];
        }, 2000);
      }
      // title error
      if (this.title.length > 40) {
        this.errors.push('Title is too long!!!');
        setTimeout(() => {
          this.errors = [];
        }, 2000);
      }
      // // name error
      // if (this.name === '') {
      //   this.errors.push('Name is required');
      //   setTimeout(() => {
      //     this.errors = [];
      //   }, 2000);
      // }
      // // text error
      // if (this.text === '') {
      //   this.errors.push('Please write your promise');
      //   setTimeout(() => {
      //     this.errors = [];
      //   }, 2000);
      // }
      if (this.text.length > 300) {
        this.errors.push('Maximum promise characteres 300');
        setTimeout(() => {
          this.errors = [];
        }, 2000);
      }

      // end of toast
      if (!this.errors.length) {
        let data = {
          title: this.title,
          text: this.text,
          name: this.name,
          color: this.color,
          fontColor: this.fontColor,
        };
        try {
          axios.post(this.url, data);
          this.title = '';
          this.text = '';
          window.location.reload();
          window.scrollTo(0, 0);
        } catch (err) {
          console.log(`ERROR: ${err}`);
        }
      }
    },
  },
};
</script>

<style scoped>
.form-section {
  height: 100%;
  width: 100vw;
  background-color: rgba(0, 0, 0, 0.6);
  position: relative;
  z-index: 2;
}
.form-container {
  margin: 0 auto;
  height: 500px;
  width: 90%;
  max-width: 600px;
  margin: 0 auto;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
@media screen and (min-width: 768px) {
  .form-container {
    margin-top: 60px;
  }
}
.form {
  height: 100%;
  width: 100%;
  max-width: 600px;
  border-radius: 2rem;
  padding: 1rem;
  padding: 1rem;
  text-align: center;
}

.card-content {
  height: 100%;
  width: 100%;
  padding: 1rem;
  position: relative;
}
.form-input {
  display: flex;
  flex-direction: column;
}
.title {
  margin: 1rem auto 0.5rem auto;
  font-size: 1.5rem;
}
.title input,
.name input {
  height: 2rem;
  text-align: center;
  font-size: 1.5rem;
}
.underline {
  height: 2px;
  width: 100%;
  margin: 1rem auto;
}
.options {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 3rem;
  margin-top: 1rem;
}
.color {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 1rem;
}
.text {
  margin-top: 1rem;
}
.text textarea {
  height: 160px;
  resize: none;
  font-size: 1.5rem;
}
.name {
  position: absolute;
  bottom: 5rem;
  left: 50%;
  transform: translateX(-50%);
}

.btn {
  font-size: 1rem;
  position: absolute;
  bottom: 1rem;
  left: 50%;
  transform: translateX(-50%);
}
.btn {
  position: absolute;
  bottom: 1rem;
  left: 50%;
  transform: translateX(-50%);
  width: 200px;
  height: 40px;
  border: none;
  outline: none;
  color: #111;
  font-size: 17px;
  background: white;
  cursor: pointer;
  z-index: 0;
  border-radius: 10px;
}

.btn:before {
  content: '';
  background: linear-gradient(
    45deg,
    #ff0000,
    #ff7300,
    #fffb00,
    #48ff00,
    #00ffd5,
    #002bff,
    #7a00ff,
    #ff00c8,
    #ff0000
  );
  position: absolute;
  top: -2px;
  left: -2px;
  background-size: 400%;
  z-index: -1;
  filter: blur(5px);
  width: calc(100% + 4px);
  height: calc(100% + 4px);
  animation: glowing 20s linear infinite;
  opacity: 0;
  transition: opacity 0.3s ease-in-out;
  border-radius: 10px;
}

.btn:active {
  color: #000;
}

.btn:active:after {
  background: transparent;
}

.btn:hover:before {
  opacity: 1;
}

.btn:after {
  z-index: -1;
  content: '';
  position: absolute;
  width: 100%;
  height: 100%;

  left: 0;
  top: 0;
  border-radius: 10px;
}

@keyframes glowing {
  0% {
    background-position: 0 0;
  }
  50% {
    background-position: 400% 0;
  }
  100% {
    background-position: 0 0;
  }
}
.errors {
  position: absolute;
  top: -50px;
  left: 0;
  width: 100%;
  height: 120px;
  z-index: -2;
  margin: 0 auto;
}

.toast {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 80%;
  height: 25px;
  background: #ff0062;
  color: white;
  margin: 10px auto;
  border-radius: 10px;
  padding: 1rem;
}

/* enter transitions */
.toast-enter-active {
  animation: wobble 0.5s ease;
}
/* leave transitions */
.toast-leave-to {
  opacity: 1;
  transform: translateY(-60px);
}
.toast-leave-active {
  transition: all 0.1s ease;
}
@keyframes wobble {
  0% {
    transform: translateY(-100px);
    opacity: 0;
  }
  50% {
    transform: translateY(0px);
    opacity: 1;
  }
  60% {
    transform: translateX(8px);
    opacity: 1;
  }
  70% {
    transform: translateX(-8px);
    opacity: 1;
  }
  80% {
    transform: translateX(4px);
    opacity: 1;
  }
  90% {
    transform: translateX(-4px);
    opacity: 1;
  }
  100% {
    transform: translate(0px);
    opacity: 1;
  }
}
</style>
