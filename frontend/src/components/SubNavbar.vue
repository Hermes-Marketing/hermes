<template>
  <nav class="sub-navbar" v-if="subItems.length">
    <div class="sub-navbar-menu">
      <div class="sub-navbar-start">
        <a
          v-for="item in subItems"
          :key="item"
          class="sub-navbar-item"
          href="#"
        >
          {{ item }}
        </a>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "SubNavbar",
  props: {
    subItems: {
      type: Array,
      required: true,
    },
  },
};
</script>

<style scoped>
.sub-navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.5rem;
  background-color: #444;
  color: #fff;
}
.sub-navbar-item {
  color: #fff;
  text-decoration: none;
  margin: 0 0.5rem;
}
.sub-navbar-item:hover {
  text-decoration: underline;
}
</style>
