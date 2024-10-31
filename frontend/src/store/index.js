import { createStore } from "vuex";

const store = createStore({
    state() {
        return {
            cityData: {},
        };
    },
    mutations: {
        setCityData(state, payload) {
            state.cityData = payload;
        },
    },
    actions: {
        updateCityData({ commit }, cityData) {
            commit("setCityData", cityData);
        },
    },
    getters: {
        getCityData: (state) => (city) => {
            return state.cityData[city] || [];
        },
    },
});

export default store;
