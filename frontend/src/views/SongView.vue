<template>
    <div v-if="song">
        <p><strong>Name:</strong> {{ song.name }}</p>
        <p><strong>Artist:</strong> {{ song.artist_id }}</p>
    </div>
</template>


<script>
import { defineComponent } from 'vue';
import { mapGetters, mapActions } from 'vuex';

export default defineComponent({
    name: 'Song-view',
    props: ['id'],
    async created() {
        try {
            await this.viewSong(this.id);
        } catch (error) {
            console.error(error);
            this.$router.push('/dashboard');
        }
    },
    computed: {
        ...mapGetters({ song: 'stateSong' }),
    },
    methods: {
        ...mapActions(['viewSong', 'deleteSong']),
        async removeSong() {
            try {
                await this.deleteSong(this.id);
                this.$router.push('/dashboard');
            } catch (error) {
                console.error(error);
            }
        }
    },
});
</script>
