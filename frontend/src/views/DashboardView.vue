<template>
    <div>
        <section>
            <h1>Add new song</h1>
            <hr /><br />

            <form @submit.prevent="submit">
                <div class="mb-3">
                    <label for="name" class="form-label">Name:</label>
                    <input type="text" name="name" v-model="form.name" class="form-control" />
                </div>
                <div class="mb-3">
                    <label for="artist_id" class="form-label">Artist id:</label>
                    <textarea name="artist_id" v-model="form.artist_id" class="form-control"></textarea>
                </div>
                <button type="submit" class="btn btn-primary">Submit</button>
            </form>
        </section>

        <br /><br />

        <section>
            <h1>Songs</h1>
            <hr /><br />
            <div v-if="songs.length">
                <div v-for="song in songs" :key="song.id" class="notes">
                    <div class="card" style="width: 18rem;">
                        <div class="card-body">
                            <ul>
                                <li><strong>Song Name:</strong> {{ song.name }}</li>
                                <li><strong>Author Id:</strong> {{ song.artist_id }}</li>
                                <li><router-link :to="{ name: 'Song', params: { id: song.id } }">View</router-link></li>
                            </ul>
                        </div>
                    </div>
                    <br />
                </div>
            </div>

            <div v-else>
                <p>Nothing to see. Check back later.</p>
            </div>
        </section>
    </div>
</template>

<script>
import { defineComponent } from 'vue';
import { mapGetters, mapActions } from 'vuex';

export default defineComponent({
    name: 'Dashboard-view',
    data() {
        return {
            form: {
                artist_id: '',
                name: '',
            },
        };
    },
    created: function () {
        return this.$store.dispatch('getSongs');
    },
    computed: {
        ...mapGetters({ songs: 'stateSongs' }),
    },
    methods: {
        ...mapActions(['createSong']),
        async submit() {
            await this.createSong(this.form);
        },
    },
});
</script>