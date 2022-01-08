<template>
  <div>
    <div class="promise-container">
      <button @click="openModal" class="btn">Make a promise</button>
      <div class="background-color"></div>
      <div class="card">
        <div
          v-for="(promise, index) in allPromises"
          :key="promise.id"
          :class="`card${index}`"
          class="promises"
          :style="
            index <= 5
              ? { marginTop: index * 10 + 'px', background: promise.color }
              : { marginTop: 60 + 'px', background: promise.color }
          "
        >
          <div class="card-content" :style="{ color: promise.fontColor }">
            <h2 class="title">{{ promise.title }}</h2>
            <div
              class="underline"
              :style="{ background: promise.fontColor }"
            ></div>
            <p class="text">{{ promise.text }}</p>
            <div class="name" v-if="promise.name">
              <p>{{ promise.name }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="container"></div>
  </div>
</template>

<script>
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
gsap.registerPlugin(ScrollTrigger);

// import axios from 'axios';
export default {
  props: ['allPromises'],

  updated() {
    if (this.allPromises.length) {
      this.animations();
    }
  },
  data() {
    return {
      url: 'api/v1/promise-api/',
      style: '',
    };
  },
  methods: {
    openModal() {
      this.$emit('openModal');
    },
    animations() {
      if (this.allPromises) {
        const singleCard = [];
        const backgorundColor = [];
        this.allPromises.map((card, idx) => {
          if (idx > 0) {
            singleCard.push(`card${idx}`);
            backgorundColor.push(card.color);
          }
        });

        const tl = gsap.timeline({
          scrollTrigger: {
            trigger: '.promise-container',
            start: 'top top',
            toggleActions: 'play none reverse pause',
            scrub: true,
            pinSpacing: true,
            pin: '.promise-container',
            end: () => '+=' + document.querySelector('.card').offsetWidth * 10,
          },
        });
        const reverseCardsArray = singleCard.reverse();
        // const reverseBackgorundColorArray = backgorundColor.reverse();
        for (let i = 0; i < reverseCardsArray.length; i++) {
          tl.to(`.${reverseCardsArray[i]}`, {
            yPercent: 100 * 2,
            opacity: 1,
          })
            .to(
              `.background-color`,
              {
                background: backgorundColor[i],
                opacity: 0.4,
              },
              '<'
            )
            .to(
              `.btn`,
              {
                background: backgorundColor[i],
              },
              '<'
            )
            .to(
              `.${reverseCardsArray[i - 1]}`,
              {
                boxShadow: '20px 20px 20px red',
              },
              '<'
            );
        }
      }
    },
  },
};
</script>

<style scoped>
.promise-container {
  width: 100%;
  height: 100vh;
  position: fixed;
  /* position: relative; */
  display: grid;
  place-content: center;
  overflow: hidden;
}
.card {
  width: 100vw;
  min-height: 300px;
  z-index: 1;
  position: relative;
}
.background-color {
  position: absolute;
  z-index: -1;
  height: 100%;
  width: 100%;
  background: hsla(293, 40%, 92%, 0.947);
}
.promises {
  height: 500px;
  width: 90%;
  max-width: 600px;
  margin: 0 auto;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  border-radius: 20px;
}
.card-content {
  height: 100%;
  width: 100%;
  padding: 1rem;
  position: relative;
}
.title {
  margin: 1rem auto 0.5rem auto;
  font-size: 2rem;
  text-align: center;
}
.underline {
  height: 2px;
  width: 100%;
  margin: 0.5rem auto;
}
.text {
  font-size: 1.5rem;
}
.name {
  font-size: 1.5rem;
  position: absolute;
  bottom: 2rem;
  left: 50%;
  transform: translateX(-50%);
}

.btn {
  position: absolute;
  top: 20px;
  left: 50%;
  transform: translateX(-50%);
}
.btn {
  width: 220px;
  height: 50px;
  border: none;
  outline: none;
  color: #111;
  font-size: 17px;
  background: white;
  cursor: pointer;
  position: relative;
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
.btn {
  position: absolute;
  top: 20px;
  left: 50%;
  transform: translateX(-50%);
}
</style>
