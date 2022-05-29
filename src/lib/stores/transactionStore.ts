import {readable} from 'svelte/store';
import axios from '$lib/api/index';

export const audits = readable(null, function start(set) {
    const auditTrail = getTransaction();
    set(auditTrail);

    return function stop() {
        console.log('Ended');
    }
});

async function getTransaction() {
    try {
        return await axios.get('/transaction');
    } catch (e) {
        console.log(e);
    }
}