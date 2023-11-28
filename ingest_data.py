import pandas as pd

measurements_path = 'ForC_measurements.csv'
sites_path = 'ForC_sites.csv'

measurements = pd.read_csv(measurements_path, encoding="utf-8")
sites = pd.read_csv(sites_path, encoding='cp1252')

print(measurements.head())
print(sites.head())

merged = pd.merge(measurements, sites, on='sites.sitename', how='outer')

final_cols = [
    'sites.sitename',
    'lat',
    'lon',
    'mean',
    'stand.age',
    'dominant.veg',
    'scientific.name',
    'variable.name',
    'city',
    'state',
    'country',
    'soil.classification',
    'continent',
    'biogeog',
    'FAO.ecozone',
]

merged.to_csv('ForC_merged.csv', index=False)


all_var_names = [
    'deadwood_OM', 'biomass_ag_OM', 'biomass_root_C', 'soil_C',
    'deadwood_down_OM', 'biomass_ag_understory_OM', 'biomass_root_OM',
    'organic.layer_OM', 'biomass_ag_woody_OM', 'biomass_ag_foliage_OM', 'NEE_C',
    'R_eco_C', 'GPP_C', 'biomass_OM', 'leaf_pN', 'ANPP_0_OM',
    'ANPP_litterfall_1_OM', 'ANPP_woody_stem_OM', 'ANPP_woody_OM',
    'BNPP_root_coarse_OM', 'BNPP_root_fine_OM', 'BNPP_root_OM', 'NPP_1_OM',
    'NPP_woody_C', 'biomass_ag_C', 'biomass_C', 'organic.layer_C', 'ANPP_1_OM',
    'ANPP_0_C', 'BNPP_root_C', 'NPP_0_C', 'biomass_ag_foliage_C',
    'biomass_ag_woody_C', 'biomass_root_coarse_C', 'biomass_root_fine_C',
    'ANPP_woody_stem_C', 'ANPP_foliage_C', 'ANPP_1_C', 'ANPP_woody_branch_C',
    'ANPP_woody_C', 'ANPP_2_C', 'BNPP_root_coarse_C', 'BNPP_root_fine_C',
    'NPP_1_C', 'R_soil_C', 'R_auto_root_C', 'R_het_soil_C', 'ANPP_litterfall_0_C',
    'BNPP_root.turnover_fine_C', 'NPP_litter_C', 'ANPP_litterfall_0_OM',
    'soil_C2N', 'NEP_C', 'biomass_ag_understory_C', 'delta.agb_OM',
    'woody.mortality_ag_OM', 'ANPP_folivory_C', 'R_auto_C', 'R_auto_foliage_C',
    'R_auto_wood_C', 'leaf_C2N', 'ANPP_foliage_OM', 'ANPP_repro_OM', 'NPP_2_C',
    'NPP_understory_C', 'ANPP_2_OM', 'deadwood_standing_OM',
    'biomass_root_coarse_OM', 'biomass_root_fine_OM', 'ANPP_litterfall_2_OM',
    'ANPP_woody_branch_OM', 'deadwood_C', 'O.horizon_C', 'litter_C', 'LAI',
    'soil_OM', 'ANPP_litterfall_1_C', 'delta.agb_C', 'woody.mortality_ag_C',
    'R_auto_ag_C', 'TBCF_C', 'NPP_5_C', 'NPP_understory_OM', 'NPP_2_OM',
    'total.ecosystem_C', 'R_het_litter_C', 'ANPP_repro_C', 'NPP_3_C', 'soil_pC',
    'ANPP_folivory_OM', 'NPP_0_OM', 'deadwood_down_C', 'leaf_pCa', 'leaf_pK',
    'leaf_pMg', 'leaf_pP', 'stem_pN', 'root_pN', 'NEE_cum_C', 'GPP_cum_C',
    'R_eco_cum_C', 'NPP_3_OM', 'N.mineralization', 'total.ecosystem_2_C',
    'deadwood_standing_C', 'leaf_pC', 'foliage_pN', 'NPP_4_C', 'root_pC',
    'stem_pC', 'litter_OM', 'delta.O.horizon_C'
]

var_names_to_keep = [
    'biomass_ag_C',
]

merged = merged.loc[merged['variable.name'].isin(var_names_to_keep)]

print('marge', merged.head())

forest_carbon_plots_by_lat_long = merged[final_cols]
forest_carbon_plots_by_lat_long.to_csv('forest_carbon_plots_by_lat_long.csv', index=False)

# Aggregate using average value of the mean column
mean_forest_carbon_plots_by_lat_long = forest_carbon_plots_by_lat_long[['sites.sitename', 'mean', 'lat', 'lon']].groupby(['sites.sitename', 'lat', 'lon']).mean().reset_index()

# Merge the grouped data back to the original so that it has lat lon still
a = len(mean_forest_carbon_plots_by_lat_long)
b = len(forest_carbon_plots_by_lat_long)
mean_forest_carbon_plots_by_lat_long.to_csv('mean_forest_carbon_plots_by_lat_long.csv', index=False)
