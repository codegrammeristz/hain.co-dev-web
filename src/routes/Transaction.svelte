<script lang="ts">
    import NavbarWithSearch from "$lib/components/navbars/NavbarWithSearch.svelte";
    import ButtonBack from "$lib/components/buttons/ButtonBack.svelte";
    import TransactionTableRow from "$lib/components/tableRows/TransactionTableRow.svelte";
    import {audits} from "$lib/stores/transactionStore";
    import TableLoadingScreen from "$lib/components/otherComponents/TableLoadingScreen.svelte";

    let recordNumber = 1;
    const counter = (): number => {
        return recordNumber++;
    }

    const identifyType = (code) => {
        switch (code) {
            case 1:
                return "ORDER"

            case 2:
                return "BUY"

            case 3:
                return "ADMIN/STAFF"
        }
    }
</script>

<svelte:head>
    <link href="https://fonts.googleapis.com/css2?family=Karla:wght@600&display=swap" rel="stylesheet"/>
</svelte:head>

<NavbarWithSearch />

<div class="container">
    <div class="columns has-text-centered pt-5">
        <div class="column is-4 has-text-centered">
            <ButtonBack link="Database"/>
        </div>
        <div class="column is-4">
            <p class="text has-text-link">
                Transactions
            </p>
        </div>
    </div>

    <div class="column is-10 is-offset-1 pl-5 pt-0">
        <table class="table is-hoverable is-fullwidth">
            <thead>
                <tr>
                    <th>No.</th>
                    <th>Agent</th>
                    <th>Description</th>
                    <th>Amount</th>
                    <th>Type</th>
                    <th>Date</th>
                </tr>
            </thead>

            {#await $audits}
                <TableLoadingScreen/>
            {:then audit}
                {#each audit.data as info}
                    <TransactionTableRow
                        id={counter()}
                        agent={info.transaction_agent}
                        description={info.transaction_description}
                        amount={info.transaction_amount}
                        type={identifyType(info.transaction_type)}
                        date={info.transaction_date}/>
                {/each}
            {:catch err}
                <p>{err.message}</p>
            {/await}
        </table>
    </div>
</div>

<style>
    .text {
        font-family: 'Karla', sans-serif;
        font-size: 40px;
    }

    table {
        font-family: 'Karla', sans-serif;
        font-size: 20px;
    }
</style>