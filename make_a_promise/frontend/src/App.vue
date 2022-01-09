<template>
  <div id="app">
    <router-view />
  </div>
</template>

<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Mulish:ital,wght@0,300;0,400;0,500;0,600;0,700;1,800&display=swap');

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Mulish', sans-serif;
}
body,
html {
  height: 100%;
  width: 100%;
}
#app {
  top: 0;
  left: 0;
  position: fixed;
  overflow: hidden;
  width: 100%;
  height: 100%;
}
</style>
