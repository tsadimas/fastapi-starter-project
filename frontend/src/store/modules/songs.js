import axios from 'axios';

const state = {
  songs: null,
  song: null
};

const getters = {
  stateSongs: state => state.songs,
  stateSong: state => state.song,
};

const actions = {
  async createSong({dispatch}, song) {
    await axios.post('songs/', song);
    await dispatch('getSongs');
  },
  async getSongs({commit}) {
    let {data} = await axios.get('songs/');
    commit('setSongs', data);
  },
  async viewSong({commit}, id) {
    let {data} = await axios.get(`songs/${id}`);
    commit('setSong', data);
  },
  // eslint-disable-next-line no-empty-pattern
  async updateSong({}, song) {
    await axios.patch(`songs/${song.id}`, song.form);
  },
  // eslint-disable-next-line no-empty-pattern
  async deleteSong({}, id) {
    await axios.delete(`songs/${id}`);
  }
};

const mutations = {
  setSongs(state, songs){
    state.songs = songs;
  },
  setSong(state, song){
    state.song = song;
  },
};

export default {
  state,
  getters,
  actions,
  mutations
};