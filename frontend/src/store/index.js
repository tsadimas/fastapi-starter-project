import { createStore } from "vuex";

import songs from './modules/songs';

export default createStore({
  modules: {
    songs,
  }
});