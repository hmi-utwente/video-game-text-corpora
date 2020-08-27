_BinaryGFFIDList_h = """//::///////////////////////////////////////////////////////////////////////////
//::
//::  Binary Generic File Format ID List
//::
//::  Copyright (c) 2006, BioWare Corp.
//::
//::///////////////////////////////////////////////////////////////////////////
//::
//::  BinaryGFFIDList.h
//::
//::///////////////////////////////////////////////////////////////////////////
//::
//::  Created By:       Ross Gardner
//::  Created On:       Feb 21, 2006
//::
//::  Maintained By: 
//::
//::///////////////////////////////////////////////////////////////////////////
//::
//::  Description:      The Binary GFF system relies on IDs instead of string entries
//::                    for accessing and storing values with the GFF file.  This
//::                    requires that those IDs be assigned and stored in a central
//::                    place that is accessible by the system loading in those
//::                    files as well as the system that saves them out (creates
//::                    them in the first place)
//::
//::                    This file is a list of these IDs followed by a comment that
//::                    gives a name and a brief description about what the ID entry
//::                    is for.
//::
//::                    When creating a new GFF type reserve a range of IDs for that file
//::                    so that the IDs are easy to read. Reserving 1000 values should
//::                    be enough and will allow us to have over four million ranges
//::
//::                    Do not reuse IDs. If an ID needs to be removed then comment it out and
//::                    leave it there. Add new ranges at the end of all the ranges and new fields
//::                    in a range after all the other fields.
//::
//::  Format:           The following is the format of each entry:
//::
//::            GFF_****  =  ##, // $$ | $$$$ 
//::
//::                    where:
//::
//::            **** -is the remainder of the #define name that will be used in code 
//::                  to read the field.
//::            ##   -is the number (ID) of the entry, should be exactly 1 more than
//::                  the previous entry (entries start at 1 and 0 is always invalid).
//::                  Do not leave this field blank.
//::            $$   -is the name of the entry as you want it to show up in the GFF
//::                  editor.  If nothing is entered it will use the **** entry as is.
//::            $$$$ -is what will show up in the tooltip on the entry in the GFF
//::                  editor.  It should be a very brief description of the field.
//::                  If nothing is entered then the tool tip will be blank.
//::
//::
//::///////////////////////////////////////////////////////////////////////////

#ifndef BINARYGFFIDLIST_H
#define BINARYGFFIDLIST_H

enum GFFID 
{
GFF_INVALIDENTRY                 =   0, // Invalid Entry | Invalid Entry

// Begin Generic Range
GFF_TAG                          =   1,  // Tag | object tag - should be unique
GFF_NAME                         =   2,  // Name | the name of the object - as it shows up in 
GFF_TEMPLATERESREF               =   3,  // Template Reference | The template file for this object
GFF_POSITION                     =   4,  // Position | The position of this object
GFF_ORIENTATION                  =   5,  // Orientation | The orientation of this object
GFF_UINT8_LIST                   =   6,  // UINT8 List | UINT8 List
GFF_INT8_LIST                    =   7,  // INT8 List | INT8 List
GFF_UINT16_LIST                  =   8,  // UINT16 List | UINT16 List
GFF_INT16_LIST                   =   9,  // INT16 List | INT16 List
GFF_UINT32_LIST                  =   10, // UINT32 List | UINT32 List
GFF_INT32_LIST                   =   11, // INT32 List | INT32 List
GFF_UINT64_LIST                  =   12, // UINT64 List | UINT64 List
GFF_INT64_LIST                   =   13, // INT64 List | INT64 List
GFF_FLOAT32_LIST                 =   14, // FLOAT32 List | FLOAT32 List
GFF_FLOAT64_LIST                 =   15, // FLOAT64 List | FLOAT64 List
GFF_VECTOR3F_LIST                =   16, // Vector3f List | Vector3f List
GFF_VECTOR4F_LIST                =   17, // Vector4f List | Vector4f List
GFF_QUATERNIONF_LIST             =   18, // Quaternionf List | Quaternionf List
GFF_ECSTRING_LIST                =   19, // ECString List | ECString List
GFF_COLOR4F_LIST                 =   20, // Color4f List | Color4f List
GFF_NAME_HASH                    =   21, // Name hash | the hash value of the object's name
GFF_TEXT                         =   22, // Text | Localizable text
GFF_OBJECT_ID                    =   23, // Object Id | The object id for this object.

GFF_TS_PROPERTY                  =   900, // Field for adding saved toolset property | Toolset property
GFF_TS_PROPERTY_NAME             =   901, // Property name for toolset property auto-save | Property name
GFF_TS_PROPERTY_ATOM             =   902, // Property atom for toolset property auto-save | Property atom
GFF_TS_PROPERTY_VALUE            =   903, // Property value for toolset property auto-save | Property value
GFF_TS_PROPERTY_CHILDREN         =   904, // Property child list for toolset property auto-save | Child list
GFF_TS_PROPERTY_VARTYPE          =   905, // Property type for toolset property auto-save | Property type

// generic range reserved up to 999

// Begin Item Range
GFF_ITEM_BASEID                  =   1000, // Base Item ID | base Id of the item
GFF_ITEM_COST                    =   1001, // Item Cost | cost of the item
GFF_ITEM_STACKSIZE               =   1002, // Stack Size | maximum stack size of the item
GFF_ITEM_STOLEN                  =   1003, // Item Stolen | true(1) or false(0) if the item can be stolen or not
GFF_ITEM_PLOT                    =   1004, // Plot Item | tru(e(1) or false(0) if it is a plot item or not
GFF_ITEM_IDENTIFIED              =   1005, // Item Identified | true(1) or false(0) if it is identified or not
GFF_ITEM_CHARGES                 =   1006, // Number of Charges | number of charges this item starts out with
GFF_ITEM_MODELVARIATION          =   1007, // Model Variation | variation number on the item model - combines in 3 digit format to complete the name  ie. 001
GFF_ITEM_DESCRIPTION             =   1008, // Item Description | description that shows up in the game for the item
GFF_ITEM_PROPERTYLIST            =   1009, // Property List | List of properties on the item
GFF_ITEM_MATERIAL                =   1010, // Designer material | Index into materialtypes 2da
GFF_ITEM_ABILITYID               =   1011, // Item ability Id | Ability this item can use
GFF_ITEM_ABILITYPWR              =   1012, // DEPRECATE: Item ability Power | Power level for this item's ability
GFF_ITEM_PROPERTIES              =   1013, // List of Item Properties | List of item property indices to itemprps 2da
GFF_ITEM_PROPERTY_POWERS         =   1014, // List of Item Property powers | Property power levels for each item property
GFF_ITEM_PROPERTY_EFFECTID       =   1015, // List of Item effect ids | List of effect references for each item property
// X_NO_LONGER_USED_X_GFF_ITEM_ONHIT_EFFECTID          =   1016, // On Hit abilities 
// X_NO_LONGER_USED_X_GFF_ITEM_ONHIT_POWER             =   1017,
GFF_ITEM_PROPERTY_VFXID          =   1018, // List of Item VFX ids | List of VFX id associated with each item property.
GFF_ITEM_SUBITEMS_RESREFS        =   1019, // List of sub-item resrefs | List of resrefs of items attached/contained in this item
GFF_ITEM_CRAFTINGRECIPEID        =   1020, // Type of recipe this is | The type of crafting recipe this item is
GFF_ITEM_BASECOST                =   1021, // The base cost of an item
// item range reserved up to 1999

// Begin item properties range
GFF_ITEM_PROP_PARAM1                  =   2000,  // Param1 | A parameter that can be used in certain properties
GFF_ITEM_PROP_PROPERTYNAME            =   2001,  // Name | The name of the property
GFF_ITEM_PROP_SUBTYPE                 =   2002,  // Subtype | The subtype of the property
GFF_ITEM_PROP_COSTTABLE               =   2003,  // Cost Table | Which cost table to use?
GFF_ITEM_PROP_COSTVALUE               =   2004,  // Cost Value | The value of the cost?
GFF_ITEM_PROP_PARAM1VALUE             =   2005,  // Param1 Value | The value of param1 if it is used
GFF_ITEM_PROP_CHANCEAPPEAR            =   2006,  // Chance Appear | The chance for this item to appear
// item properties range reserved up to 2999

// Begin environment properties range
GFF_ENV_WORLD                    =   3000, // World | struct "WRLD". top-level world layout struct
GFF_ENV_WORLD_NAME               =   3001, // name | string. Name of World as seen in env editor
GFF_ENV_WORLD_AREA_LIST          =   3002, // AreaList | list of area structs
GFF_LVL_CHILD_LIST               =   3003, // ChildList | Level Object Child List
GFF_LVL_FILE_OBJECT_VERSION      =   3004, // LVL File object version.
GFF_LVL_CHANGETIME               =   3005, // LVL document last change time.

GFF_ENV_AREA                     =   3010, // Area | struct "AREA" representing an Area Layout
GFF_ENV_AREA_ID                  =   3011, // id | int32 Area ID
GFF_ENV_AREA_NAME                =   3012, // name | string. Name of Area Layout as seen in env editor
GFF_ENV_AREA_FILE                =   3013, // file | string.
GFF_ENV_AREA_ENVIRONMENTSETTINGS =   3014, // EnvironmentSettings | struct "ENVS". environment settings TBD
GFF_ENV_AREA_NAVIGATION_INFO_FILE=   3015, // NavigationInfoFile | string. extensionless name of pathfinding file for area
GFF_ENV_AREA_ROOM_LIST           =   3016, // RoomList | list of room structs
GFF_ENV_AREA_ROOM_LIST_ELEMENT   =   3017, // RoomList | struct "AROM". room belonging to an area's roomlist
GFF_ENV_AREA_POSITION            =   3018, // position | vector. position of area
GFF_ENV_AREA_ROTATION            =   3019, // rotation | quaternion. orientatio of area
GFF_ENV_AREA_PATHFINDING_EXPORT  =   3020, // PathfindingExporterInfo | struct "ARPA" containing area pathfinding struct
GFF_ENV_AREA_PATHFINDING_VISINFO =   3021, // PathfindingVisInfo | list of int32 areaIDs
GFF_ENV_AREA_PATHFINDING_VISINFO_COUNT   =   3022, // count | int32 number of elements in visinfo. Deprecated.
GFF_ENV_AREA_FRAME_BUFFER_EFFECT =   3023, // Struct containing FB info (see GFF_CUTSCENE_ACTION_FRAME_BUFFER_EFFECT_ for contents)
GFF_ENV_AREA_CENTER				 =   3024, // Area center | vector. center point of area
GFF_ENV_AREA_SKYDOME_MODEL       =   3025, // Area skydome | resref for the skydome model 
GFF_ENV_AREA_FRAME_BUFFER_EFFECT_LIST    =   3026, // FBE List | list of GFF_ENV_AREA_FRAME_BUFFER_EFFECT structs
GFF_ENV_AREA_GLOBALWIND_RESREF   =   3027, // ResRef to global WND file
GFF_ENV_AREA_LOCALWIND_LIST      =   3028, // List of local WND files
GFF_ENV_AREA_PATHFINDING_COSTS   =   3029, // list of ints indicating cost of pathfinding points.

GFF_ENV_ROOM                     =   3030, // Room | struct "ROOM".
GFF_ENV_ROOM_ID                  =   3031, // id | int32. Room ID
GFF_ENV_ROOM_NAME                =   3032, // name | string. Name of Room as seen in Env Editor
GFF_ENV_ROOM_FILE                =   3033, // file | string. extensionless filename of room layout file
GFF_ENV_ROOM_ENVIRONMENTSETTINGS =   3034, // EnvironmentSettings | struct "ENVS" environment settings for a room. TBD.
GFF_ENV_ROOM_POSITION            =   3035, // position | vector. Position of room relative to its parent area
GFF_ENV_ROOM_ROTATION            =   3036, // rotation | quaternion. Orientation of room relative to its parent area
GFF_ENV_ROOM_PATHFINDING_GRIDSEPARATION  =   3037, // PathGridSep | float32 pathfinding grid separation distance
GFF_ENV_ROOM_PATHFINDING_CHARACTERHEIGHT =   3038, // PathCharHeight | float32 pathfinding character height
GFF_ENV_ROOM_PATHFINDING_CLEARANCE       =   3039, // PathClearance | float32 pathfinding overhead clearance
GFF_ENV_ROOM_PATHFINDING_EXPORT          =   3040, // PathfindingExporterInfo | Struct "ROPA" containing pathfinding structs
GFF_ENV_ROOM_PATHFINDING_VISINFO         =   3041, // PathfindingVisInfo | list of int32 roomIDs of rooms visible to this room.
GFF_ENV_ROOM_PATHFINDING_VISINFO_COUNT   =   3042, // count | int32 number of rooms in visinfo list. Deprecated.
GFF_ENV_ROOM_PATH_GRID_FILE      =   3043, // PathGridFile | string. extensionless filename of pathfinding grid file.
GFF_ENV_ROOM_PATHCONNECTION_LIST =   3044, // PathConnectionList | list of int32 roomIDs of rooms connected to this room
GFF_ENV_ROOM_PATHCONNECTION      =   3045, // Connection | deprecated
GFF_ENV_ROOM_PATHCONNECTION_ID   =   3046, // id | deprecated
GFF_ENV_ROOM_VISIBILITY_LIST     =   3047, // VisibilityList | int of int32 roomIDs of rooms visible to this room
GFF_ENV_ROOM_VISIBILITY          =   3048, // Visible | deprecated
GFF_ENV_ROOM_VISIBILITY_ID       =   3049, // id | deprecated
GFF_ENV_ROOM_MODEL_LIST          =   3050, // ModelList | list of roommodel structs.
GFF_ENV_ROOM_LIGHT_LIST          =   3051, // LightList | list of roomlight structs
GFF_ENV_ROOM_MODEL_LIST_ELEMENT  =   3052, // ModelList Element | struct "RLIT". model belonging to a room model list
GFF_ENV_ROOM_LIGHT_LIST_ELEMENT  =   3053, // LightList Element | struct "RMDL". light belonging to a room light list
GFF_ENV_ROOM_DYNSHADOW_DIRECTION =   3054, // DynShadowDirection | vector3 direction of dynamic shadows in this room
GFF_ENV_ROOM_DYNSHADOW_ENABLED   =   3055, // DynShadowsEnabled | int8 treated as boolean, indicates if room has dynamic shadows

GFF_ENV_MODEL_PATHFINDING_OVERLAPPED =3056,// Overlapped | int8 boolean indicating if this model may overlap other models for pathfinding
GFF_ENV_MODEL_SHOW_HIGH_LOD      =   3057, // Show High LOD | boolean indicating if this model should render in the editor with high LOD instead of low
GFF_ENV_MODEL_SNAP_TO_TERRAIN    =   3058, // Snap To Terrain | boolean indicating if this model should snap to terrain as it is painted or moved
GFF_ENV_MODEL_SCALE			     =   3059, // Scale | float. Scale factor of the model relative to its original size

GFF_ENV_MODEL                    =   3060, // Model | struct "MDL". 
GFF_ENV_MODEL_ID                 =   3061, // id | int32 model ID
GFF_ENV_MODEL_NAME               =   3062, // name | string. Name of model object used by graphics engine.
GFF_ENV_MODEL_FILE               =   3063, // file | string. Name of model mmh file without extension.
GFF_ENV_MODEL_POSITION           =   3064, // position | vector. Position of model relative to parent room.
GFF_ENV_MODEL_ROTATION           =   3065, // rotation | quaternion. Orientation of model relative to parent room.
GFF_ENV_MODEL_PATHFINDING_NORMAL =   3066, // pathfindingnormal | vector. Direction of pathfinding normal

GFF_ENV_LIGHT                    =   3067, // Light | struct "LIT"
GFF_ENV_LIGHT_ID                 =   3068, // id | int32 light ID
GFF_ENV_LIGHT_NAME               =   3069, // name | string. Name of light object used by graphics engine
GFF_ENV_LIGHT_POSITION           =   3070, // position | vector. Position of light relative to parent room.
GFF_ENV_LIGHT_ROTATION           =   3071, // rotation | quaternion. Orientation of light relative to parent room.
GFF_LIGHT_COLOR                  =   3072, // color | vector. color of the light
GFF_LIGHT_ISDYNAMIC              =   3073, // dynamic | int8 boolean. True for dynamic lights, false for static
GFF_LIGHT_TYPE                   =   3074, // light type | int32 enumerated value. See ILight.h for values
GFF_LIGHT_POINT_RADIUS           =   3075, // point light radius | float32 radius of point lights.
GFF_LIGHT_COLOR_MULTIPLIER       =   3076, // color multiplier | float32 intensity multiplier for the light
GFF_LIGHT_BAKED                  =   3077, // baked | int8 boolean. True for baked light used for lightmapping, false for non-baked lights used in game
GFF_LIGHT_EFFECT                 =   3078, // effect | Light effect (replaces GFF_LIGHT_ISDYNAMIC and GFF_LIGHT_BAKED in new files)
GFF_LIGHT_AFFECT_DOMAIN          =   3079, // character/level light | int32 enumerated value. See class LvlLight in RenderLvlObject.h

GFF_AREAGRID_NAVINFO             =   3080, // NavInfo | struct "NAVI". top-level NavInfo struct for roomgrid pathfinding info
GFF_AREAGRID_ROOMNAME            =   3081, // RoomName | string. 
GFF_AREAGRID_GRIDNAVINFO         =   3082, // GridNavInfo | list of ModelGrid structs
GFF_AREAGRID_MODELGRID           =   3083, // ModelGrid | struct "MDGD" containing model grid info
GFF_AREAGRID_GRIDID              =   3084, // GridID | int32 ID of a modelgrid
GFF_AREAGRID_MODELID             =   3085, // ModelID | string. Object name of the model associated with this grid
GFF_AREAGRID_NBCOLUMNS           =   3086, // Columns | int32 number of columns
GFF_AREAGRID_NBROWS              =   3087, // Rows | int32 number of row
GFF_AREAGRID_CELLSIZE            =   3088, // CellSize | float32 size of each pathfinding cell in the grid
GFF_AREAGRID_CLEARANCE           =   3089, // HeightClearance | float32 height clearance of each cell
GFF_AREAGRID_BASEPOS             =   3090, // BasePosition | vector position of the model grid origin corner (relative to the room?)
GFF_AREAGRID_NORMAL              =   3091, // Normal | vector normal to the grid surface
GFF_AREAGRID_DATA                =   3092, // Data | float32 list of grid data. interpret rows and colums according to the NBROWS and NBCOLUMNS
GFF_AREAGRID_HEIGHT              =   3093, // Data | float32 list of grid data. interpret rows and colums according to the NBROWS and NBCOLUMNS
GFF_AREAGRID_ABSTRACTION_SECTORSIZE =   3094, // Size | Abstraction Layer Sector Size
GFF_AREAGRID_ABSTRACTION_SECTORS = 3095,    // Sector Data | Abstraction layer sector data
GFF_AREAGRID_ABSTRACTION_MEMORY  = 3096,    // Memory Data | Abstraction layer memory data
GFF_AREAGRID_ID                  =   3097, // Id | int32 link ID
GFF_AREAGRID_CELLID              =   3098, // CellId | int32 cell ID

GFF_ENV_ROOM_CONNECTIVITY_LIST   =   3099, // Connectivity list | int of int32 roomIDs of rooms connected to this room

GFF_LIGHT_SPOT_INNER_ANGLE       =   3100, // spot inner angle | float32 angle of the spot's inner falloff rim
GFF_LIGHT_SPOT_OUTER_ANGLE       =   3101, // spot outer angle | float32 angle of the spot's outer rim
GFF_LIGHT_SPOT_DISTANCE          =   3102, // spot distance | float32 distance of target from light

GFF_ENV_LIGHT_PROBE              =   3103, // Light Probe | struct "PRB"
GFF_ENV_LIGHT_PROBE_ENVMAP       =   3104, // Environment Map Resource Name | string

GFF_ENV_LIGHT_NUM_SAMPLES        =   3105, // Soft Shadows | number of rays
GFF_ENV_LIGHT_SIZE               =   3106, // Soft Shadows | size of light emitter
GFF_DYNAMICSHADOW_VECTOR_GAME    =   3107, // Dynamic shadow vector, as used by the game.  Different than the dynamic shadow data saved/loaded by the toolset

GFF_ENV_LIGHT_PROBE_ID           =   3108, // light probe ID | int32 ID used in editor document only, not for game.

GFF_ENV_MODEL_CUT_AWAY_OVERRIDE  =   3109, // cutaway override | uint8 : 0 - no override; 1 - all parts do not cut away; 2 - all parts cut away

GFF_AREAGRID_AREA                =   3110, // Struct "AREA" | top level struct for area pathfinding info

GFF_AREAGRID_SOUND_DATA          = 3114,    // Data | byte list of grid data, sound material type. interpret rows and colums according to the NBROWS and NBCOLUMNS
GFF_AREAGRID_ABSTRACTION_SNUMREG = 3115,    // Region Count | Abstraction layer sector region count
GFF_AREAGRID_ABSTRACTION_SADDR   = 3116,    // Region Data Offset | Abstraction layer region data offset

GFF_AREAGRID_LIGHT_SUBSET_DATA8   = 3117,    // Light subset data | byte list of light subset (of containing room) that affects this point, interpret rows and colums according to the NBROWS and NBCOLUMNS
GFF_AREAGRID_LIGHT_SUBSET_DATA16   = 3118,   // Light subset data | ushort list of light subset (of containing room) that affects this point, interpret rows and colums according to the NBROWS and NBCOLUMNS

GFF_LIGHT_CAN_BE_OCCLUDED          = 3119,    // Can be occluded | bool indicating whether light can be occluded (character lights only as of 2008.10.22)

GFF_AREAGRID_CELLPADDING           = 3120, // CellPading | float32 padding distance at the lower corner of the pathfinding patch

//GFF_AREAGRID_AREA_ID             =   3111, // areaID | int32 ID of area referenced in area pathfinding info struct
//GFF_AREAGRID_ROOMS               =   3112, // roomlist | list of area pathfinding room structs
//GFF_AREAGRID_ROOM                =   3113, // roomstruct | Struct "ROOM". top level struct for area pathfinding room info
//GFF_AREAGRID_ROOM_ID             =   3114, // roomID | int32 ID of room
//GFF_AREAGRID_ROOM_NUMBER_OF_LINKS=   3115, // linkcount | int32 number of links for this room
//GFF_AREAGRID_LINKS               =   3116, // linklist | list of Link structs
//GFF_AREAGRID_LINK                =   3117, // linkstruct | Struct "LINK". top level struct for an area pathfinding link
//GFF_AREAGRID_LINK_ID             =   3118, // linkID | int32 ID of the link
//GFF_AREAGRID_LINK_CELL_ID        =   3119, // link cell ID | int32 link's cell ID
//GFF_AREAGRID_LINK_ROOM_ID        =   3120, // link room ID | int32 link's room ID
//GFF_AREAGRID_LINK_NEIGHBOR_IDS   =   3121, // link neighbor ID list | list of int32 neighbor IDs for this link

GFF_ENV_AREA_CHUNK_ISCHUNK       =   3122, // ischunk | int8, 1 for chunks, 0 for normal room. If chunked, the roomlist must have rowcount*colcount elements.
GFF_ENV_AREA_CHUNK_ROWCOUNT      =   3123, // chunk row count | int32 number of rows (y) of chunks
GFF_ENV_AREA_CHUNK_COLCOUNT      =   3124, // chunk column count| int32 number of columns (x) of chunks
GFF_ENV_AREA_CHUNK_WIDTH         =   3125, // chunk width | float32 width (x-axis) of each chunk
GFF_ENV_AREA_CHUNK_HEIGHT        =   3126, // chunk height | float32 height (y axis) of each chunk
GFF_ENV_AREA_LAYOUT_NAME         =   3127, // layout name | 7-char string for the name of the area layout
GFF_ENV_AREA_STARTPOINT_NAME     =   3128, // start point name of the area
GFF_ENV_AREA_CUTOFF_HEIGHT       =   3129, // cutoff height | enumerated high/med/low universal cutoff height for the level.

GFF_LIGHT_ANIMATED_MIN_FREQUENCY =   3130, // animated maximum frequency | maximum frequency of intensity change for an animated light
GFF_LIGHT_ANIMATED_MAX_FREQUENCY =   3131, // animated maximum frequency | maximum frequency of intensity change for an animated light
GFF_LIGHT_ANIMATED_MIN_INTENSITY =   3132, // animated maximum frequency | maximum frequency of intensity change for an animated light
GFF_LIGHT_ANIMATED_MAX_INTENSITY =   3133, // animated maximum frequency | maximum frequency of intensity change for an animated light

GFF_ENV_AREA_CUTOFF_SYSTEM_ENABLED=   3134, // whether the cutoff system is enabled (DA1 defaults: exterior=false, interior=true)

GFF_ENV_MINIMAP_TEXTURE_MAP_COORDS =  3137, // Texture coordinates of the bottom right corner of the map (0 - 1)
GFF_ENV_MINIMAP_LOWER_LEFT_POINT   =  3138, // World coordinates of lower left point in minimap.
GFF_ENV_MINIMAP_UPPER_RIGHT_POINT  =  3139, // World coordinates of upper right point in minimap.

GFF_ENV_ROOM_LOWER_LEFT_POINT    =   3140, // lower left point | coordinate for the lower left point of the room
GFF_ENV_ROOM_UPPER_RIGHT_POINT   =   3141, // upper right point | coordinate for the upper right point of the room
GFF_ENV_AREA_FORCE_CHARACTER_LIGHTING=3142,// ---DEPRECATED--- Temporary flag for forcing character lighting. In prep. for E3 2008.

GFF_ENV_AREA_SUNLIGHT_CAN_BE_OCCLUDED_CHAR = 3148, // Character sunlight can be occluded
GFF_ENV_AREA_SUNLIGHT_COLOR_CHAR =   3149, // Character sunlight color
GFF_ENV_AREA_SUNLIGHT_DIRECTION  =   3150, // SunlightDirection | vector, the direction of the sunlight
GFF_ENV_AREA_SUNLIGHT_ENABLED    =   3151, // SunlightEnabled | int8 treated as boolean, indicates if room has sunlight
GFF_ENV_AREA_SUNLIGHT_COLOR      =   3152, // SunlightColor | Color, the color of the sunlight
GFF_ENV_AREA_SUNLIGHT_COLORMULT  =   3153, // SunlightColorMultiplier | float32, multiplier for the sunlight color

GFF_TERRAIN_CHUNK				 =   3154, // Terrain Chunk | Struct defining a chunk of a terrain level
GFF_TERRAIN_CHUNK_LIST           =   3155, // Terrain Chunk List | List of structs of chunk objects.
GFF_TERRAIN_CHUNK_CELL_POSITION_X=   3156, // Chunk X Position | Starting Chunk Offset in X direction
GFF_TERRAIN_CHUNK_CELL_POSITION_Y=   3157, // Chunk Y Position | Starting Chunk Offset in Y direction
GFF_TERRAIN_CHUNK_LENGTH         =   3158, // Chunk Length | Length of the chunk
GFF_TERRAIN_CHUNK_WIDTH          =   3159, // Chunk Width  | Width of the chunk
GFF_TERRAIN_CHUNK_TEXEL_SIZE     =   3160, // Chunk Texel Size | Texel size of the chunk
GFF_TERRAIN_CHUNK_BLENDPAGE_SIZE =   3161, // Chunk blend page Size | Blend page size of the chunk
GFF_TERRAIN_CHUNK_SECTOR_ID      =   3162, // Sector ID | Sector ID related to the chunk
//GFF_ENV_AREA_SUNLIGHT_ROTATION   =   3163, // [NOT CURRENTLY USED] SunlightRotation | float32, the sunlight rotation size (degrees)

GFF_ENV_ROOM_LIGHT_VIS_LIST      =   3164, // Light Vis List | List of Room IDs for rooms that lights in this room effect
GFF_ENV_FOG_COLOR                =   3165, // Distance Fog Color | Vector3f - Color of the distance fog
GFF_ENV_FOG_MAX_DISTANCE         =   3166, // Distance Fog Max Distance | FLOAT32 - The distance at which the fog reach max density (from the camera)
GFF_ENV_FOG_MAX_INTENSITY        =   3167, // Distance Fog Max Intensity | FLOAT32 - The maximum density for distance fog
GFF_ENV_FOG_ENABLED              =   3168, // Distance Fog Enabled | int8 boolean - Whether or not distance fog is enabled
GFF_ENV_FOG_MIN_DISTANCE         =   3169, // Distance Fog Min Distance | FLOAT32 - The distance from the camera at which the the fog begins

GFF_ENV_MODEL_NAME_CHANGED       =   3170, // name changed | boolean indicating if this model name was changed by the user.

GFF_ENV_VEGETATION               =   3171, // vegetation | struct "VEGT"
GFF_ENV_CREATURE                 =   3172, // test creature | struct "CRE"

GFF_ENV_CAMERA                   =   3200, // Camera | struct Camera info
GFF_ENV_CAMERA_PIVOTDISTANCE     =   3201, // Camera Pivot Distance | float32 camera pivot distance
GFF_ENV_STANDALONE               =   3202, // Standalone Children | struct of children
GFF_ENV_LIST_AREA                =   3202, // Standalone Area List | list of Area structs
GFF_ENV_LIST_ROOM                =   3203, // Standalone Room List | list of Room structs
GFF_ENV_LIST_MODEL               =   3204, // Standalone Model List | list of Model structs
GFF_ENV_LIST_LIGHT               =   3205, // Standalone Light List | list of Light structs

GFF_ENV_PFCONTAINER_LAYOUTNAME   =   3210, // Pathfinding container layout name.
GFF_ENV_PFCONTAINER_EXPORTDATA   =   3211, // Pathfinding container export data.
GFF_ENV_PFCONTAINER_DATAVERSION  =   3212, // Pathfinding container export data version.
GFF_ENV_PFCONTAINER_VISINFO      =   3213, // Pathfinding container visualization info.

GFF_RIMTREE_ROOT_NODE            =   3290, // RIMTree Root Node | struct, Root of Resource RIM Tree
GFF_RIMTREE_RIM_LIST             =   3291, // RIM List | list of RIM names, RIMs required for node
GFF_RIMTREE_CHILD_LIST           =   3292, // Child List | list of RIMTree Node structs, children of node
GFF_RIMTREE_NODE_TAG             =   3293, // Node TAG | string, TAG of node
GFF_RIMTREE_NODE_RESREF          =   3294, // Node ResRef | string, ResRef of node

GFF_ENV_GROUP                    =   3300, // Group | struct, a group of level objects
GFF_ENV_GROUP_NAME               =   3301, // Group Name | string, the name of a group

GFF_ENV_SP_GROUP				 =   3302, // Start Point Group | struct, a group of Start Point
GFF_ENV_SP_GROUP_NAME			 =   3303, // Start Point Group Name | string, the name of group
GFF_ENV_SP						 =   3304, // Start Point | struct
GFF_ENV_SP_FILE					 =   3305, // Start Point Name | string

GFF_ENV_OBJECT_VISIBLE           =   3310, // Visible | uint8 bool indicating if this object is visible in the editor
GFF_ENV_OBJECT_LOCKSELECTION     =   3311, // LockSelection | int32 enumeration. 0 = normal, 1 = unselectable, 2 = exclusive select

GFF_ENV_MODEL_INSTANCEID         =   3320, // InstanceID | string to pass to Graphics::IBaseObject::SetInstanceID() after creating an object
GFF_ENV_MODEL_BOUNDS_CENTER      =   3321, // BoundCenter | vector3 representing the center of a model's bounding sphere
GFF_ENV_MODEL_BOUNDS_RADIUS      =   3322, // BoundRadius | float representing the radius of a model's bounding sphere
GFF_ENV_MODEL_LIGHTMAP_ATLAS     =   3323, // LightmapAtlas | string, the name of the lightmap atlas for this model
GFF_ENV_MODEL_LIGHTMAP_OFFSET_SCALE = 3324, // LightmapOffsetAndScale | vector4 containing lightmap data offset and scale to use when accessing atlas texture
GFF_ENV_MODEL_LIGHTMAP_PART_ID   =   3235, // LightmapPartID | uint32, the part id this lightmap atlas info corresponds to
GFF_ENV_MODEL_LIGHTMAP_ATLAS_LIST = 3326,  // LightmapAtlasList | list of lightmap atlas info -- (one per part)

GFF_LVL_LIGHTMAP_SIZE_MULTIPLIER =   3330, // Lightmap Size Multiplier | Lightmap Texture Size Multiplier

GFF_LVL_LIGHTMAP_LAST_UPDATED_LIST=  3331, // Baked light update list | list of layouts and their last update time
GFF_LVL_LIGHTMAP_LAST_UPDATED    =   3332, // Baked light update element | last update time for a layout
GFF_LVL_LIGHTMAP_FILESPEC        =   3333, // Filename for the lightmap
GFF_LVL_LIGHTING_VERSION         =   3334, // Lighting Version for point light selection algorithm.

GFF_LVL_AO_COLOR_MIN             =   3340, // Ambient Occlusion Min Color | color3 Ambient Occlusion 
GFF_LVL_AO_COLOR_MAX             =   3341, // Ambient Occlusion Max Color | color3 Ambient Occlusion 
GFF_LVL_AO_SAMPLES_MIN           =   3342, // Ambient Occlusion Min Samples | int32 Ambient Occlusion 
GFF_LVL_AO_SAMPLES_MAX           =   3343, // Ambient Occlusion Max Samples | int32 Ambient Occlusion 
GFF_LVL_AO_ADAPTSAMPLEENABLED    =   3344, // Ambient Occlusion AdaptSampleEnabled | int8 as boolean Ambient Occlusion 
GFF_LVL_AO_ADAPTSAMPLEACCURACY   =   3345, // Ambient Occlusion AdaptSampleAccuracy | float32 Ambient Occlusion 
GFF_LVL_AO_ADAPTSAMPLESMOOTH     =   3346, // Ambient Occlusion AdapthSampleSmooth | float32 Ambient Occlusion 
GFF_LVL_AO_CONEANGLE             =   3347, // Ambient Occlusion Cone Angle | float32 Ambient Occlusion 
GFF_LVL_AO_MAXRAYLENGTH          =   3348, // Ambient Occlusion Max Ray Length | float32 Ambient Occlusion 
GFF_LVL_AO_EXPONENT              =   3349, // Ambient Occlusion Exponent | float32 Ambient Occlusion 

GFF_ENV_TREE                     =   3350, // Model | struct "MDL". 
GFF_ENV_TREENODE_ID              =   3351, // id | int32 model ID
GFF_ENV_TREE_NAME                =   3352, // name | string. Name of model object used by graphics engine.
GFF_ENV_TREE_FILE                =   3353, // file | string. Name of model mmh file without extension.
GFF_ENV_ROOM_TREENODE_LIST       =   3354, // TreeNodeList | list of room tree node structs.
GFF_ENV_AREA_TREECONTROLLER_LIST =   3355, // TreeControllerList | list of tree controller global resource structs.
GFF_ENV_TREE_SCALE			     =   3356, // Scale | float. Scale factor of the model relative to its original size
GFF_ENV_AREA_TREECONTROLLER_ID   =   3357, // Global resource ID, used by SPT instance
GFF_ENV_TREE_PAINTED_LIST        =   3358, // Painted Tree List | struct "TLST"
GFF_ENV_TREE_PAINTED_POSITION    =   3359, // Painted tree position | vector3
GFF_ENV_TREE_PAINTED_ROTATION    =   3360, // Painted tree rotation around z axis | float32
GFF_ENV_TREE_PAINTED_SCALE       =   3361, // Painted tree scaling factor | float32
GFF_ENV_SCATTER_OBJECTS          =   3362, // Scatter object | struct "SCAT"
GFF_ENV_SCATTEROBJECT_FILE       =   3363, // file | string | Scatter objects .mmh prototype file.
GFF_ENV_SCATTER_INSTANCE         =   3364, // Scatter object instance
GFF_ENV_SCATTER_INSTANCE_LIST    =   3365, // Scatter object instance list
GFF_ENV_SCATTEROBJECT_LIST       =   3366, // ScatterObjectList | List of room scatter objects
GFF_ENV_SCATTEROBJECT_ID         =   3367, // ScatterObjectID | Reference to the instance's scatter object
GFF_ENV_SCATTEROBJ_IGNORE_MAX_DENSITY=  3368, // int8 bool | Ignore max density setting on scatter object's controller
GFF_ENV_SCATTEROBJ_MAX_DENSITY   =   3369, // float | Maximum density setting on scatter object's controller
GFF_ENV_SCATTEROBJ_MIN_SCALE     =   3370, // float | Minimum scale setting on scatter object's controller
GFF_ENV_SCATTEROBJ_MAX_SCALE     =   3371, // float | Maximum scale setting on scatter object's controller
GFF_ENV_SCATTEROBJ_ORIENT        =   3372, // int8 bool | Orientation flag on scatter object's controller
GFF_ENV_SCATTEROBJ_PROTOTYPE     =   3373, // string | Scatter objects prototype model (.mmh)
GFF_ENV_SCATTEROBJ_MSI_DATA      =   3374, // string | Scatter objects instance data file (.msi)
GFF_ENV_TREE_COLOR_TINT          =   3375, // color | tinting color for a tree
GFF_ENV_SCATTEROBJ_SOUND_TYPE    =   3376, // sound | sound played when creature moves through scattered objects
GFF_ENV_TREE_COLOR_LEVEL_TINT    =   3377, // color | tinting color for trees in an area. On export this represents a Vector4 with color XYZ and the intensity in W
GFF_ENV_TREE_COLOR_LEVEL_INTENSITY=  3378, // float | multiplies the color values in the tint. This ID isn't used for export, the value is exported in the ID above.
GFF_ENV_TREE_DRAW_DISTANCE       =   3379, // int8 | Tree instance draw distance setting (low, medium, high)

GFF_TERRAIN_EXPORT_AREA          =   3400, // Terrain Export Area | Struct defining an exportable region of a terrain level
GFF_TERRAIN_EXPORT_AREA_LIST     =   3401, // Terrain Export Area List | List of structs of terrainexportarea objects.
GFF_TERRAIN_AREA_CELL_POSITION_X =   3403, // Cell X Position | Starting Cell Offset in X direction
GFF_TERRAIN_AREA_CELL_POSITION_Y =   3404, // Cell Y Position | Starting Cell Offset in Y direction
GFF_TERRAIN_AREA_CELL_POSITION_Z =   3405, // Cell Z Position | Starting Cell Offset in Z direction
GFF_TERRAIN_AREA_CELL_SIZE_X     =   3406, // Cell X Size | Number of Cells in X direction
GFF_TERRAIN_AREA_CELL_SIZE_Y     =   3407, // Cell Y Size | Number of Cells in Y direction
GFF_TERRAIN_AREA_CELL_SIZE_Z     =   3408, // Cell Z Size | Number of Cells in Z direction
GFF_TERRAIN_AREA_BORDER_CELL_WIDTH=  3409, // Border Cell Width | Width of area layout border in cells
GFF_TERRAIN_AREA_VISTA_CELL_WIDTH=   3410, // Vista Cell Width | Width of area layout vista in cells
GFF_TERRAIN_AREA_LIGHTMAP_SIZE   =   3411, // Terrain Export Area Lightmap Size | Width of lightmap textures
GFF_TERRAIN_AREA_LIGHTMAP_SIZE_VISTA=3412, // Terrain Export Area Vista Lightmap Size | Width of lightmap textures for vista chunks
GFF_TERRAIN_AREA_SUBDIVIDE_BY    =   3413, // Terrain Export Area Chunk Subdivision Factor | Number of times to subdivide each chunk on export.

GFF_ENV_MODEL_PARTGROUP          =   3500, // Part group this model belongs to.
GFF_ENV_MODEL_LIGHTMAPONLY       =   3501, // Lightmap only flag for a model.
GFF_ENV_MODEL_LIGHTMAP_FLAG      =   3502, // Lightmap enable
GFF_ENV_MODEL_EXPORT_FLAG        =   3503, // Export enable
GFF_ENV_MODEL_DEFAULT_ANIMATION  =   3504, // The name of the looping animation to play.
GFF_ENV_MODEL_BLEND_TREE_NAME    =   3505, //The name of the blend tree the default animation is in (should be based on the chunk/room)
GFF_ENV_MODEL_USER_PARAM_LIST    =   3506, // User param list | list of user param structs.
GFF_ENV_MODEL_USER_PARAM_NAME    =   3507, // User param name | the name of the user param
GFF_ENV_MODEL_USER_PARAM_VALUE   =   3508, // User param value | the value of the user param

GFF_LVL_WATER                    =   3600, // Water | struct "AQUA". 
GFF_LVL_WATER_SIZE_X             =   3601, // float | Water quad dimension in the X axis
GFF_LVL_WATER_SIZE_Y             =   3602, // float | Water quad dimension in the Y axis
GFF_LVL_WATER_MAX_TESSELLATION    =   3603, // int | Water max tessellation level
GFF_LVL_WATER_MESH_ID            =   3604, // int | Water mesh ID
GFF_LVL_WATER_NORMAL_MAP         =   3605, // string | Water waves normal map
__deprecated__GFF_LVL_WATER_HEIGHT_MAP         =   3606,
GFF_LVL_WATER_DEEP_COLOR         =   3607, // Color | Deep Water Color
GFF_LVL_WATER_SHALLOW_COLOR      =   3608, // Color | Shallow Water Color
GFF_LVL_WATER_WAVE_FREQ_1        =   3609, // float | Wave 0 frequency
GFF_LVL_WATER_WAVE_AMPL_1        =   3610, // float | Wave 0 amplitude
GFF_LVL_WATER_WAVE_DIRECTION_1   =   3611, // float | Wave 0 direction angle
GFF_LVL_WATER_WAVE_SPEED_1       =   3618, // float | Wave 0 direction angle
GFF_LVL_WATER_WAVE_FREQ_2        =   3612, // float | Wave 1 frequency
GFF_LVL_WATER_WAVE_AMPL_2        =   3613, // float | Wave 1 amplitude
GFF_LVL_WATER_WAVE_DIRECTION_2   =   3614, // float | Wave 1 direction angle
GFF_LVL_WATER_WAVE_SPEED_2       =   3619, // float | Wave 0 direction angle
GFF_LVL_WATER_WAVE_FREQ_3        =   3615, // float | Wave 2 frequency
GFF_LVL_WATER_WAVE_AMPL_3        =   3616, // float | Wave 2 amplitude
GFF_LVL_WATER_WAVE_DIRECTION_3   =   3617, // float | Wave 2 direction angle
GFF_LVL_WATER_WAVE_SPEED_3       =   3620, // float | Wave 0 direction angle
__deprecated__GFF_LVL_WATER_REFLECTIVITY       =   3621,
__deprecated__GFF_LVL_WATER_FOAM_HEIGHT        =   3622,
__deprecated__GFF_LVL_WATER_SUBDIVISION_DEPTH_TOLERANCE = 3623,
GFF_LVL_WATER_SHALLOW_DEPTH      =   3624, // float | shallow water depth
__deprecated__GFF_LVL_WATER_FOAM_COLOR         =   3625,
GFF_LVL_WATER_WALKABLE_DEPTH     =   3626, // float | The maximum depth walkable for characters
GFF_LVL_WATER_WALL_HEIGHT        =   3627, // float | The collision wall height which is placed at walkable depth
GFF_LVL_WATER_OPACITY_FALLOFF    =   3628,
GFF_LVL_WATER_SUNLIGHT_SPECULAR_POWER   = 3629,
GFF_LVL_WATER_SPECULAR_MULTIPLIER       = 3630,
GFF_LVL_WATER_SPECULAR_FALLOFF          = 3631,
GFF_LVL_WATER_COLORIZE_TRANSPARENCY     = 3632,
GFF_LVL_WATER_OVERRIDE_REFLECTION       = 3633,
GFF_LVL_WATER_ENABLE_SPEC               = 3634,


GFF_LVL_WIND                     =   3700, // struct
GFF_LVL_WIND_ID                  =   3701, // int32 | ID for the wind object.
GFF_LVL_WIND_NAME                =   3702, // string | User defined object name.
GFF_LVL_WIND_ISGLOBAL            =   3710, // bool | This wind object is global
GFF_LVL_WIND_REGIONRADIUS        =   3711, // float | 
GFF_LVL_WIND_REGIONFALLOFF       =   3712, // float | 
GFF_LVL_WIND_SPTSTRENGTH         =   3713, // float | 
GFF_LVL_WIND_SPTGUST_MINPERCENT  =   3714, // float | 
GFF_LVL_WIND_SPTGUST_MAXPERCENT  =   3715, // float | 
GFF_LVL_WIND_SPTGUST_MINDURATION =   3716, // float | 
GFF_LVL_WIND_SPTGUST_MAXDURATION =   3717, // float | 
GFF_LVL_WIND_SPTBENDANGLE        =   3718, // float |
GFF_LVL_WIND_CLOTH_RESPONSE      =   3719, // float |
GFF_LVL_WIND_CLOTH_RESPONSE_LMT  =   3720, // float |
GFF_LVL_WIND_CLOTH_STRENGTH      =   3721, // float |
GFF_LVL_WIND_CLOTH_GUST_STRENGTH_MIN =   3722, // float |
GFF_LVL_WIND_CLOTH_GUST_STRENGTH_MAX =   3723, // float |
GFF_LVL_WIND_CLOTH_GUST_DURATION_MIN =   3724, // float |
GFF_LVL_WIND_CLOTH_GUST_DURATION_MAX =   3725, // float |
GFF_LVL_WIND_CLOTH_GUST_INTERVAL_MIN =   3726, // float |
GFF_LVL_WIND_CLOTH_GUST_INTERVAL_MAX =   3727, // float |
GFF_LVL_WIND_CLOTH_GUST_DIR_CHANGE =   3728, // float |
GFF_LVL_WIND_CLOTH_GUST_AXIS_RATIO =   3729, // vector3 |
GFF_LVL_WIND_SPTGUST_FREQUENCY = 3730,


GFF_LVL_COLLISION_WALL_INFO         =   3730, // Collision wall information
GFF_LVL_COLLISION_WALL_VERTICIES    =   3731, // uint32 List
GFF_LVL_COLLISION_WALL_VERTICIES_V2 =   3732, // Vector3f List

GFF_LVL_MINIMAP_POSITION_X            =  3740, // Lower x edge of the minimap region | float
GFF_LVL_MINIMAP_POSITION_Y            =  3741, // Lower y edge of the minimap region | float
GFF_LVL_MINIMAP_SIZE_X                =  3742, // x size of the minimap region | float
GFF_LVL_MINIMAP_SIZE_Y                =  3743, // y size of the minimap region | float

GFF_ENV_STAT_PHYS                    =  3744, // Optimized static physics blob
GFF_ENV_STAT_PHYS_DATA               =  3745, // Optimized static physics data

GFF_LVL_LIGHT_SUBSET_LIST             =  3800, // Light Subset | a list of light IDs (the subset of all lights that affect a point)
GFF_LVL_LIGHT_SUBSET_ENTRY            =  3801, // Light Subset Entry | ID of a light that is in this subset
GFF_LVL_LIGHT_SUBSET_TOTAL_ENTRIES    =  3802, // Light Subset Total Entries | Number of lights in all subsets for this room

// environment properties range reserved up to 3999

// begin animation range
GFF_ANIMATION_NODENAME               =  4000, // Node Name | The name of the animation node  // DEPRECATED
GFF_ANIMATION_TARGET                 =  4001, // Target | The target type of the animation data
GFF_ANIMATION_SOURCETYPE             =  4002, // Source Type | The type of the animation source
GFF_ANIMATION_ELEMENTSPERENTRY       =  4003, // Elements | The number of elements per entry
GFF_ANIMATION_NODEDATA               =  4004, // Node Data | The data for this animation node
GFF_ANIMATION_NODELIST               =  4005, // Node List | The list of node for this animation
GFF_ANIMATION_NAME                   =  4006, // Name | The file name of the animation  // DEPRECATED
GFF_ANIMATION_GENERALANIMNAME        =  4007, // General Animation NAme | The name of the general animation  // DEPRECATED
GFF_ANIMATION_HASGOBANIM             =  4008, // Has GOB Animation | 1 if it has Game Object animation 0 otherwise
GFF_ANIMATION_ANIMLENGTH             =  4009, // Length | The length in time of the animation
GFF_ANIMATION_COMBATRANGE            =  4010, // Combat Range | The appropriate distance from the target for this animation
GFF_ANIMATION_ISADDITIVE             =  4011, // Is Additive | Is this animation additive
GFF_ANIMATION_ISOVERRIDE             =  4012, // Is Override | Is this an override animation
GFF_ANIMATION_OVERRIDEPRIORITY       =  4013, // Override Priority | The priority of the override animation
GFF_ANIMATION_NAME_HASH              =  4014, // General animation name hash | The hash ID of the general animation name
GFF_ANIMATION_NODENAME_HASH          =  4015, // Animation node name hash | The hash ID of the animation node name
GFF_ANIMATION_EVENT_TIME             =  4016, // Animation event time | The time of the animation event
GFF_ANIMATION_EVENT_ID               =  4017, // Animation event ID | Identifier for the animation event type
GFF_ANIMATION_EVENT_TARGET           =  4018, // Animation event target | Target system to receive the animation event
GFF_ANIMATION_EVENT_STRING           =  4019, // Animation event string | Meta information about the event
GFF_ANIMATION_EVENT_LIST             =  4020, // Animation event list | List of animation events
GFF_ANIMATION_TREE                   =  4021, // Animation tree node list | List of animation tree nodes
GFF_ANIMATION_TREE_NAME              =  4022, // Animation tree name | Name of the animation blend tree
GFF_ANIMATION_TREE_NODE              =  4023, // Animation tree node list | List of animation tree nodes
GFF_ANIMATION_TREE_NODE_NAME         =  4024, // Node name | Animation tree node name
GFF_ANIMATION_TREE_NODE_FILE         =  4025, // Animation filename | Animation tree node filename
GFF_ANIMATION_TREE_NODE_WEIGHT       =  4026, // Node initial weight | Animation tree node initial weight
GFF_ANIMATION_TREE_NODE_FLAGS        =  4027, // Node flags | Animation tree node flags
GFF_ANIMATION_TREE_NODE_FIRST_CHILD  =  4028, // First child index | Index of the first child in the node array
GFF_ANIMATION_TREE_NODE_NUM_CHILDREN =  4029, // Number of children | Number of children
GFF_ANIMATION_TREE_NODE_PARENT       =  4030, // Parent node | Index of parent node
GFF_ANIMATION_BLENDCURVE_ANIMFROM    =  4031,
GFF_ANIMATION_BLENDCURVE_ANIMTO      =  4032,
GFF_ANIMATION_BLENDCURVE_DATA        =  4033,
GFF_ANIMATION_BLENDCURVE_LIST        =  4034,
GFF_ANIMATION_KEY_TIME               =  4035, // Keyframe time | Time of a keyframe
GFF_ANIMATION_KEY_DATA0              =  4036, // Keyframe data | Data for a keyframe
GFF_ANIMATION_KEY_DATA1              =  4037, // Keyframe data | Data for a keyframe
GFF_ANIMATION_KEY_DATA2              =  4038, // Keyframe data | Data for a keyframe
GFF_ANIMATION_KEY_DATA3              =  4039, // Keyframe data | Data for a keyframe
GFF_ANIMATION_IGNORESCALE            =  4040, // Animation ignores animation scaling (true if cinematic animator animates for specific rigs)
// animation range reserved up to 4999

// Begin cutscene range

GFF_CUTSCENE_RUN_TIME               =  5000, // RunTime | Running time of the cutscene
GFF_CUTSCENE_END_SCRIPT             =  5001, // EndScript | Script to execute when the cutscene completes
GFF_CUTSCENE_LAYOUT                 =  5002, // Layout | The layout the cutscene takes place in
GFF_CUTSCENE_POSITION               =  5003, // Position | The initial location of the camera
GFF_CUTSCENE_ORIENTATION            =  5004, // Orientation | The initial orientation of the camera
GFF_CUTSCENE_TRANSITION_TIME        =  5005, // TransTime | The time to transition to the initial camera position
GFF_CUTSCENE_FOV                    =  5006, // Field of view | The initial field of view of the camera
GFF_CUTSCENE_BLENDTREE              =  5007, // Blend Tree | The custom blend tree for the cutscene
GFF_CUTSCENE_ANIMATIC               =  5008, // Animatic | The animatic to play instead of this cutscene
GFF_CUTSCENE_SHOWAREADYNAMICS       =  5009, // Show Area Dynamics | Allows objects in the area to show up in the scene.
GFF_CUTSCENE_STAGED                 =  5010, // Staged | Whether the cutscene is staged
GFF_CUTSCENE_LOD_CURVES             =  5011, // LOD Curves | Position curves for the LOD object
GFF_CUTSCENE_ANIM_SOUND_EVENTS      =  5012, // Anim Sound Events | Will animation sound events be played for actors in the scene.
GFF_CUTSCENE_ENABLE_LEVEL_FBES      =  5013, // Enable Level FBEs | Whether FBEs from the level show up in the cutscene
GFF_CUTSCENE_LOD_ORIGIN_POS         =  5014, // LOD Origin Position | Position origin of the LOD curves
GFF_CUTSCENE_LOD_ORIGIN_ORI         =  5015, // LOD Origin Orientation | Orientation origin of the LOD curves
GFF_CUTSCENE_FPS                    =  5016, // FPS | Frames per second
GFF_CUTSCENE_STAGE_RESREF           =  5017, // Stage ResRef | Stage ResRef
GFF_CUTSCENE_PLAY_UNTIL_VO_COMPLETES=  5018, // Play Until VO Completes | Cutscene plays until VO completes, even if that is past the end
GFF_CUTSCENE_AREA_REQUIRED          =  5019, // Requires Area | This cutscene requires its area to be loaded in order to play properly
GFF_CUTSCENE_SHADOW_RADIUS          =  5020, // Shadow Radius | Shadow Radius
GFF_CUTSCENE_LIGHT_OCCLUSION        =  5021, // Light Occlusion | Character Light Occlusion
// Don't use 5022 - it is used for the streaming blend tree in a branch that will eventually be integrated back

GFF_CUTSCENE_HENCHMAN_TAG        =  5050, // Henchman Tag | Special henchman tag - used in conversations
GFF_CUTSCENE_HENCHMAN_ACTIONS    =  5051, // Henchman Actions | Special henchman actions - used in conversation

GFF_CUTSCENE_RESOURCES           =  5100, // Resources | List of cutscene resources
GFF_CUTSCENE_RESOURCE_RESREF     =  5101, // ResRef | ResRef
GFF_CUTSCENE_RESOURCE_TYPE       =  5102, // Type | Resource Type

GFF_CUTSCENE_ACTORS                 = 5200, // Actors | List of cutscene actors
GFF_CUTSCENE_ACTOR_ID               = 5201, // ID | ID of the actor
GFF_CUTSCENE_ACTOR_MODEL_RESREF     = 5202, // ModelRef | ResRef of the model
GFF_CUTSCENE_ACTOR_DEPRECATED_1     = 5203, // Deprecated | Deprecated
GFF_CUTSCENE_ACTOR_DEPRECATED_2     = 5204, // Deprecated | Deprecated
GFF_CUTSCENE_ACTOR_DEPRECATED_3     = 5205, // Deprecated | Deprecated
GFF_CUTSCENE_ACTOR_ACTION_QUEUE     = 5206, // ActionQueue | List of actions for this actor
GFF_CUTSCENE_ACTOR_DEPRECATED_4     = 5207, // Deprecated | Deprecated
GFF_CUTSCENE_ACTOR_CREATURE_RESREF  = 5208, // Creature | ResRef of the creature
GFF_CUTSCENE_ACTOR_CAMERA_TARGET    = 5209, // Camera Target | Camera target actor ID
GFF_CUTSCENE_ACTOR_USE_POSE         = 5210,  // Use Pose | Whether this actor uses poses or not
GFF_CUTSCENE_ACTOR_POSE             = 5211,  // Pose | The pose ID for this creature
GFF_CUTSCENE_ACTOR_POSE_SPEED       = 5212,  // Pose Speed | The pose speed for this creature
GFF_CUTSCENE_ACTOR_POSE_HUMANOID    = 5213,  // Humanoid Pose | Whether this pose requires a humanoid
GFF_CUTSCENE_ACTOR_ORIGIN_POS       = 5214,  // Origin Position | The position to offset all movement and orientation from
GFF_CUTSCENE_ACTOR_ORIGIN_ORI       = 5215,  // Origin Orientation | The orientation to offset all movement and orientation from
GFF_CUTSCENE_ACTOR_MAPPING_TAG      = 5216,  // Actor mapping tag | The tag will be mapped to the actor
GFF_CUTSCENE_ACTOR_INVENTORY        = 5217,  // Inventory | The inventory bits
GFF_CUTSCENE_ACTOR_TRANSITION_DELAY = 5218,  // Transition Delay | The delay until the pose transition occurs
GFF_CUTSCENE_ACTOR_PREVIOUS_POSE    = 5219,  // Previous Pose | The previous pose to this line
GFF_CUTSCENE_ACTOR_MAPPING_REQUIRED = 5220,  // Mapping Required | Whether the mapping is required or not
GFF_CUTSCENE_ACTOR_FINAL_POS		= 5221,  // Final Position | The final position to offset all movement and orientation from
GFF_CUTSCENE_ACTOR_FINAL_ORI		= 5222,  // Final Orientation | The final orientation to offset all movement and orientation from
GFF_CUTSCENE_ACTOR_MASTER           = 5223,  // Master | Whether this is the master actor or not
GFF_CUTSCENE_ACTOR_LOD	            = 5224,  // LOD | The LOD for this creature
GFF_CUTSCENE_ACTOR_AMBIENT_ANIM		= 5225,  // Ambient Animation ID | The Ambient Animation ID for the creature
GFF_CUTSCENE_ACTOR_MODEL_SCALE		= 5226,  // Actor Model Scale | The Scale for Actor Model

GFF_CUTSCENE_ACTION_TYPE         =  5300, // Type | The type of action
GFF_CUTSCENE_ACTION_START_TIME   =  5301, // StartTime | The starting time of the action
GFF_CUTSCENE_ACTION_STOP_TIME    =  5302, // StopTime | The stopping time of the action
GFF_CUTSCENE_ACTION_CURVES       =  5303, // Curves | Curves on the action
GFF_CUTSCENE_ACTION_CATEGORY     =  5304, // Category | Action category

GFF_CUTSCENE_ACTION_CURVE_BASE_VALUE    = 5350, // Base Value | Base value of the curve
GFF_CUTSCENE_ACTION_CURVE_VERTICES      = 5351, // Vertices | List of vertices making up the curve
GFF_CUTSCENE_ACTION_CURVE_TRANSITIONS   = 5352, // Transitions | List of transitions making up the curve
GFF_CUTSCENE_ACTION_CURVE_DEPRECATED    = 5353, // Deprecated | Deprecated

GFF_CUTSCENE_ACTION_CURVE_VERTEX_TIME   = 5370, // Time | Time of the vertex
GFF_CUTSCENE_ACTION_CURVE_VERTEX_VALUE  = 5371, // Value | Value of the vertex

GFF_CUTSCENE_ACTION_CURVE_TRANSITION_TYPE       = 5380, // Transition Type | Type of transition
GFF_CUTSCENE_ACTION_CURVE_TRANSITION_CONTROL_1  = 5381, // Control Point 1 | First control point of the transition
GFF_CUTSCENE_ACTION_CURVE_TRANSITION_CONTROL_2  = 5382, // Control Point 2 | Second control point of the transition

GFF_CUTSCENE_ACTION_ANIM_ANIMATION_NAME		        = 5400, // Animation Name | Animation name
GFF_CUTSCENE_ACTION_ANIM_BLENDTREE_NAME		        = 5401, // Blend Tree Name | Blend tree name
GFF_CUTSCENE_ACTION_ANIM_SPEED				        = 5402, // Animation Speed | Animation speed
GFF_CUTSCENE_ACTION_ANIM_START_OFFSET		        = 5403, // Animation Start Offset | Starting time of the animation (offset from action start time)
GFF_CUTSCENE_ACTION_ANIM_DEPRECATED1		        = 5404, // Deprecated | Do not re-use this ID
GFF_CUTSCENE_ACTION_ANIM_PLAY_GAD	                = 5405, // Play Gad Animation | Play the Gad part of an animation
GFF_CUTSCENE_ACTION_ANIM_POSE_ANIMATION             = 5406, // Pose Animation | True if this is a special pose animation
GFF_CUTSCENE_ACTION_ANIM_LINK_TO_MOVEMENT           = 5407, // Link to Movement | Link animation speed to the velocity of the actor at this speed ratio.
GFF_CUTSCENE_ACTION_ANIM_GAD_KEYS_POSITION          = 5408, // GAD Position Keys | GAD position keys with orientation information baked in
GFF_CUTSCENE_ACTION_ANIM_GAD_KEYS_ORIENTATION       = 5409, // GAD Orientation Keys | GAD orientation keys
GFF_CUTSCENE_ACTION_ANIM_BLEND_GAD                  = 5410, // Blend GAD | Blend the GAD animation with out blending GADs (rather than adding)
GFF_CUTSCENE_ACTION_ANIM_EXTEND_GAD                 = 5411, // Extend GAD | Extend the GAD offset beyond its end time
GFF_CUTSCENE_ACTION_ANIM_LINK_TO_MOVEMENT_DISTANCES = 5412, // Link to Movement Distance | The distance over time for the link to movement
GFF_CUTSCENE_ACTION_ANIM_APPLY_TO_FUTURE_GADS       = 5413, // Apply Rotation To Future GADs | Applies the extended rotation to future gads

/* 5480 - 5519 Deprecated - Do not reuse these IDs */

GFF_CUTSCENE_ACTION_FRAME_BUFFER_EFFECT_FILE_NAME           =  5520, // DEPRECATED
GFF_CUTSCENE_ACTION_FRAME_BUFFER_EFFECT_EFFECT_NAME         =  5521, // FBE Effect | Name of the FBE
GFF_CUTSCENE_ACTION_FRAME_BUFFER_EFFECT_PARAM_LIST          =  5522, // FBE Properties | Properties of the FBE 
GFF_CUTSCENE_ACTION_FRAME_BUFFER_EFFECT_PARAM_NAME          =  5523, // FBE Property Name | Name of the FBE property
GFF_CUTSCENE_ACTION_FRAME_BUFFER_EFFECT_PARAM_VALUE         =  5524, // FBE Property Value | Value of the FBE effect property
GFF_CUTSCENE_ACTION_FRAME_BUFFER_EFFECT_PARAM_CURVE_INDEX   =  5525, // FBE Property Curve Index | Curve associated with the FBE property
GFF_CUTSCENE_ACTION_FRAME_BUFFER_EFFECT_PARAM_VECTOR_INDEX  =  5526, // FBE Vector Index | Vector index that this property is

/* 5540 - 5561 Deprecated - Do not reuse these IDs */

GFF_CUTSCENE_ACTION_SPEAK_LINE_LIPSYNCH_SET     = 5562, // Lipsynch set | FaceFX lipsynch animation set name
GFF_CUTSCENE_ACTION_SPEAK_LINE_VOBANK           = 5563, // VO Bank | Sound bank containing VO data
GFF_CUTSCENE_ACTION_SPEAK_LINE_FAHEADMOVEMENT   = 5564, // FA head moves | Facial animation head movement
GFF_CUTSCENE_ACTION_SPEAK_LINE_NOVOINGAME       = 5565, // No VO in Game | Whether to not play VO and FaceFX in game

GFF_CUTSCENE_ACTION_STAGE_CAMERA_DEFAULT_CAMERA = 5570, // Default Camera | Whether this is a camera tag or a default camera of a place tag
GFF_CUTSCENE_ACTION_STAGE_CAMERA_HENCHMAN_CAMERA= 5571, // Henchman Camera | Whether this is a henchman tag

GFF_CUTSCENE_ACTION_STAGE_PLACE_LOOK_AT         = 5580, // Look At | The place to look at

/* 5590 - 5599 Deprecated - Do not reuse these IDs */

GFF_CUTSCENE_ACTION_SHAKE_TYPE                  = 5600, // Shake Type | The type of shake
GFF_CUTSCENE_ACTION_SHAKE_DEPRECATED1           = 5601, // Deprecated | Do not re-use this ID
GFF_CUTSCENE_ACTION_SHAKE_DEPRECATED2           = 5602, // Deprecated | Do not re-use this ID
GFF_CUTSCENE_ACTION_SHAKE_NOISE_SEED            = 5603, // Seed | The seed for the noise
GFF_CUTSCENE_ACTION_SHAKE_NOISE_FREQUENCY       = 5604, // Frequency | The frequency for the noise
GFF_CUTSCENE_ACTION_SHAKE_NOISE_TYPE            = 5605, // Type | The type of noise
GFF_CUTSCENE_ACTION_SHAKE_NOISE_CORRELATED      = 5606, // Correlated | Whether the noise is correlated
GFF_CUTSCENE_ACTION_SHAKE_NOISE_ROUGHNESS       = 5607, // Roughness | The roughness of the noise
GFF_CUTSCENE_ACTION_SHAKE_NOISE_RAMP_IN         = 5608, // Ramp-In | The ramp in time for the noise
GFF_CUTSCENE_ACTION_SHAKE_NOISE_RAMP_OUT        = 5609, // Ramp-Out | The ramp out time for the noise

GFF_CUTSCENE_ACTION_ACTIVE_CAMERA_ACTOR_ID      = 5610, // Camera ID | Actor ID of the camera

GFF_CUTSCENE_ACTION_HEADTRACKING_TARGET_ID      = 5620,  // Target Id | Target Id
GFF_CUTSCENE_ACTION_HEADTRACKING_SPEED          = 5621,  // Headtracking speed | Headtracking speed
GFF_CUTSCENE_ACTION_HEADTRACKING_DEPRECATED1    = 5624,  // Deprecated | Do not re-use this ID
GFF_CUTSCENE_ACTION_HEADTRACKING_DEPRECATED2    = 5625,  // Deprecated | Do not re-use this ID
GFF_CUTSCENE_ACTION_HEADTRACKING_DEPRECATED3    = 5626,  // Deprecated | Do not re-use this ID
GFF_CUTSCENE_ACTION_HEADTRACKING_DEPRECATED4    = 5627,  // Deprecated | Do not re-use this ID
GFF_CUTSCENE_ACTION_HEADTRACKING_REALIGN_START  = 5628,  // Realign Source Head At Start | Whether we should force realign the source head at the start
GFF_CUTSCENE_ACTION_HEADTRACKING_REALIGN_CONT   = 5629,  // Realign Source Head Continuously | Whether we should realign the source head continously

GFF_CUTSCENE_ACTION_LINK_ACTOR_TARGET_ID		= 5630, // Target ID | Actor ID of the item to be linked
GFF_CUTSCENE_ACTION_LINK_ACTOR_NODE_ID			= 5631, // Node ID | The ID of the node to attach to
GFF_CUTSCENE_ACTION_LINK_ACTOR_DEPRECATED1      = 5632, // Deprecated | Do not re-use this ID
GFF_CUTSCENE_ACTION_LINK_ACTOR_DEPRECATED2      = 5633, // Deprecated | Do not re-use this ID
GFF_CUTSCENE_ACTION_LINK_ACTOR_DEPRECATED3      = 5634, // Deprecated | Do not re-use this ID
GFF_CUTSCENE_ACTION_LINK_ACTOR_DEPRECATED4      = 5635, // Deprecated | Do not re-use this ID
GFF_CUTSCENE_ACTION_LINK_ACTOR_IS_TARGET_CRUST  = 5636, // Is crust | If true, the target node ID refers to a crust and requires a lookup
GFF_CUTSCENE_ACTION_LINK_ACTOR_USE_OFFSET       = 5637, // Use Offset | Whether to use an offset

GFF_CUTSCENE_ACTION_APPLYCRUST_TARGET_ID        = 5640, // Target ID | Actor ID of the object that is the target for the crust effect

GFF_CUTSCENE_ACTION_POSE_ANIMATION_POSE         = 5650, // Pose | The pose blend tree
GFF_CUTSCENE_ACTION_POSE_ANIMATION_ANIMATION    = 5651, // Animation | The pose animation
GFF_CUTSCENE_ACTION_POSE_ANIMATION_LOOPING      = 5652, // Looping | Whether the animation is looping
GFF_CUTSCENE_ACTION_POSE_ANIMATION_OUTRO        = 5653, // Outro | Outro animation to play after the main animation
GFF_CUTSCENE_ACTION_POSE_ANIMATION_OUTRO_SPEED  = 5654, // Outro Speed | The speed of the outro animation

GFF_CUTSCENE_ACTION_SOUND_NAME                  = 5670, // Sound name | Sound event name
GFF_CUTSCENE_ACTION_SOUND_SPLINE_PARAM_NO1      = 5671, // Sound param 1 | Sound param no. 1
GFF_CUTSCENE_ACTION_SOUND_SPLINE_PARAM_NO2      = 5672, // Sound param 2 | Sound param no. 2
GFF_CUTSCENE_ACTION_SOUND_SPLINE_PARAM_NO3      = 5673, // Sound param 3 | Sound param no. 3
GFF_CUTSCENE_ACTION_SOUND_SPLINE_PARAM_NO4      = 5674, // Sound param 4 | Sound param no. 4
GFF_CUTSCENE_ACTION_SOUND_SPLINE_PARAM_NO5      = 5675, // Sound param 5 | Sound param no. 5

GFF_CUTSCENE_ACTION_CHANGEVISIBILITY_VISIBLE    = 5680, // Visible | Marks if the actor can be seen or not

/* 5690 - 5699 Deprecated - Do not reuse these IDs */

GFF_CUTSCENE_ACTION_TOGGLE_CLOTH_PHYSICS        = 5700, // Cloth | Toggle cloth physics
GFF_CUTSCENE_ACTION_TOGGLE_HAIR_PHYSICS         = 5701, // Hair | Toggle hair physics

GFF_CUTSCENE_ACTION_SET_LOD_DEPRECATED          = 5720, // LOD | Level of detail

GFF_CUTSCENE_ACTION_DRAW_WEAPON_MAIN            = 5730, // Main Weapon Drawn | Whether we should draw or sheath the main weapon
GFF_CUTSCENE_ACTION_DRAW_WEAPON_OFF             = 5731, // Off Weapon Drawn | Whether we should draw or sheath the off weapon

GFF_CUTSCENE_ACTION_PLAYMOVIE                   = 5740, // Play Bink Movie | Which movie to play

GFF_CUTSCENE_ACTION_SETGORE                     = 5750, // Gore | Gore level

// custscene range reserved up to 5999

// Begin MMH GFF range
GFF_MMH_NAME                                                        = 6000, // Name | Name
GFF_MMH_MATERIAL_OBJECT                                             = 6001, // Material Object | Material Object
GFF_MMH_MATERIAL_LIBRARY                                            = 6002, // Material Library | Material Library
GFF_MMH_RESNAME                                                     = 6003, // Resource Name | Filename of the resource
GFF_MMH_ID                                                          = 6004, // ID | ID
GFF_MMH_MODEL_HIERARCHY_MODEL_DATA_NAME                             = 6005, // Mesh Data Name | MSH File
GFF_MMH_MESH_GROUP_NAME                                             = 6006, // Mesh Group Name | Name
GFF_MMH_NODE_POINT_LIGHT_COLOR                                      = 6007, // Point Light Color | Point Light Light color
GFF_MMH_NODE_POINT_LIGHT_RADIUS                                     = 6008, // Point Light Radius | Point Light Radius
GFF_MMH_NODE_POINT_LIGHT_IS_STATIC                                  = 6009, // Point Light IsStatic | Point Light IsStatic flag
GFF_MMH_NODE_AMBIENT_LIGHT_COLOR                                    = 6010, // Ambient Light Color | Ambient Light color
GFF_MMH_NODE_EMITTER_BIRTH_RATE                                     = 6011, // Emitter Birth Rate | Emitter Birth Rate
GFF_MMH_NODE_EMITTER_BIRTH_RATE_RANGE                               = 6012, // Emitter Birth Rate Range | Emitter Birth Rate Range
GFF_MMH_NODE_EMITTER_LIFE                                           = 6013, // Emitter Life | Emitter Life
GFF_MMH_NODE_EMITTER_LIFE_RANGE                                     = 6014, // Emitter Life Range | Emitter Life Range
GFF_MMH_NODE_EMITTER_SCALE_RANGE                                    = 6015, // Emitter Scale Range | Emitter Scale Range
GFF_MMH_NODE_EMITTER_INITIAL_SPEED                                  = 6016, // Emitter Initial Speed | Emitter Initial Speed
GFF_MMH_NODE_EMITTER_INITIAL_SPEED_RANGE                            = 6017, // Emitter Initial Speed Range | Emitter Initial Speed Range
GFF_MMH_NODE_EMITTER_ACCELERATION                                   = 6018, // Emitter Acceleration | Emitter Acceleration
GFF_MMH_NODE_EMITTER_INITIAL_ROTATION_SPEED                         = 6019, // Emitter Initial Rotation Speed | Emitter Initial Rotation Speed
GFF_MMH_NODE_EMITTER_INITIAL_ROTATION_SPEED_RANGE                   = 6020, // Emitter Initial Rotation Speed Range | Emitter Initial Rotation Speed Range
GFF_MMH_NODE_EMITTER_ROTATIONAL_ACCELERATION                        = 6021, // Emitter Rotational Acceleration | Emitter Rotational Acceleration
GFF_MMH_NODE_INV_EMITTER_MOVEMENT_SPREAD_UPDATE_DELAY               = 6022, // Emitter Inverse Movement Spread Update Delay | Inverse Emitter Movement Spread Update Delay
GFF_MMH_NODE_EMITTER_SPAWN_SPREAD_X                                 = 6023, // Emitter Spawn Spread X | Emitter Spawn Spread X 
GFF_MMH_NODE_EMITTER_SPAWN_SPREAD_Y                                 = 6024, // Emitter Spawn Spread Y | Emitter Spawn Spread Y
GFF_MMH_NODE_EMITTER_MOVEMENT_SPREAD_X                              = 6025, // Emitter Movement Spread X | Emitter Movement Spread X
GFF_MMH_NODE_EMITTER_MOVEMENT_SPREAD_Y                              = 6026, // Emitter Movement Spread Y | Emitter Movement Spread Y
GFF_MMH_NODE_EMITTER_OPTIONS_BITFLAGS                               = 6027, // Emitter Bitflags | Emitter Bitflags
GFF_MMH_NODE_EMITTER_OPTIONS_BIRTHRATE_IN_PARTICLES_PER_METER       = 6028, // Emitter Birthrate In Particles Per Meter flag | Emitter Birthrate In Particles Per Meter flag
GFF_MMH_NODE_EMITTER_OPTIONS_RANDOM_INITIAL_ROTATION                = 6029, // Deprecated March 20/08
GFF_MMH_NODE_EMITTER_OPTIONS_PARTICLES_AFFECTED_BY_WIND             = 6030, // Emitter Particles Affected By Wind flag | Emitter Particles Affected By Wind flag
GFF_MMH_NODE_EMITTER_GRAVITY_MULTIPLIER                             = 6031, // Emitter Particles multiplier for gravity
GFF_MMH_NODE_EMITTER_OPTIONS_PARTICLES_FOLLOW_PATH                  = 6032, // Emitter Particles Follow Path flag | Emitter Particles Follow Path flag
GFF_MMH_NODE_EMITTER_OPTIONS_LINK_PARTICLES_TOGETHER                = 6033, // Emitter Link Particles Together flag | Emitter Link Particles Together flag
GFF_MMH_NODE_EMITTER_OPTIONS_UPDATE_ONLY_WHEN_VISIBLE               = 6034, // Emitter Update Only When Visible flag | Emitter Update Only When Visible flag
GFF_MMH_NODE_EMITTER_OPTIONS_ENABLE_PARTICLE_COLLISIONS             = 6035, // Emitter Enable Particle Collisions flag | Emitter Enable Particle Collisions flag
GFF_MMH_NODE_EMITTER_OPTIONS_INHERIT_VELOCITY_INSTEAD_OF_POSITION   = 6036, // Emitter Inherit Velocity Instead Of Position flag | Emitter Inherit Velocity Instead Of Position flag
GFF_MMH_NODE_EMITTER_ORIENTATION_BEHAVIOR                           = 6037, // Emitter Orientation Behavior | Emitter Orientation Behavior
GFF_MMH_NODE_EMITTER_PARTICLE_INHERITANCE                           = 6038, // Emitter Particle Inheritance | Emitter Particle Inheritance
GFF_MMH_NODE_AGE_MAP_COUNT                                          = 6039, // Age Map Count | Age Map Count
GFF_MMH_NODE_AGE_MAP_ELEMENT_PERCENT_LIFE_ELAPSED                   = 6040, // Age Map Element Percent Life Elapsed | Age Map Element Percent Life Elapsed
GFF_MMH_NODE_AGE_MAP_ELEMENT_SCALE_X                                = 6041, // Age Map Element Scale X | Age Map Element Scale X
GFF_MMH_NODE_AGE_MAP_ELEMENT_SCALE_Y                                = 6042, // Age Map Element Scale Y | Age Map Element Scale Y
GFF_MMH_NODE_AGE_MAP_ELEMENT_COLOR                                  = 6043, // Age Map Element Color | Age Map Element Color
// Age map multiplier values start at ID #6279
GFF_MMH_NODE_SPAWN_VOLUME_OPTIONS_BITFLAGS                          = 6044, // Spawn Volume Options Bitflags | Spawn Volume Options Bitflags
GFF_MMH_NODE_SPAWN_VOLUME_OPTIONS_SPAWN_WITHIN_VOLUME               = 6045, // Spawn Volume Options Spawn Within Volume | Spawn Volume Options Spawn Within Volume
GFF_MMH_NODE_SPAWN_VOLUME_OPTIONS_INVERT_SPAWN_VOLUME_NORMALS       = 6046, // Spawn Volume Options Invert Spawn Volume Normals | Spawn Volume Options Invert Spawn Volume Normals
GFF_MMH_TRANSLATION                                                 = 6047, // Translation | Translation
GFF_MMH_ROTATION                                                    = 6048, // Rotation | Rotation
GFF_MMH_ATTRIBUTE_NAME                                              = 6049, // Attribute Name | Attribute Name
GFF_MMH_ATTRIBUTE_SOURCE_NAME                                       = 6050, // Attribute Source Name | Attribute Source Name
GFF_MMH_EXPORT_TAG_NAME                                             = 6051, // Export Tag Name | Export Tag Name
GFF_MMH_EXPORT_EXPORT_NAME                                          = 6052, // Export Name | Export Name
GFF_MMH_EXPORT_CONTROLLER_TYPE                                      = 6053, // Export Controller Type | Export Controller Type
GFF_MMH_BOUNDING_BOX_MIN                                            = 6054, // Bounding Box Min | Bounding Box Min
GFF_MMH_BOUNDING_BOX_MAX                                            = 6055, // Bounding Box Max | Bounding Box Max
GFF_MMH_NODE_COLLISION_OBJ_DENSITY                                  = 6056, // Collision Object Density | Collision Object Density
GFF_MMH_NODE_COLLISION_OBJ_TYPE                                     = 6057, // Collision Object Type | Collision Object Type
GFF_MMH_SHAPE_TYPE                                                  = 6058, // Shape Type | Shape Type
GFF_MMH_SHAPE_PMAT_NAME                                             = 6059, // Shape PMat Name | Shape PMat Name
GFF_MMH_SHAPE_ROTATION                                              = 6060, // Shape Rotation | Shape Rotation
GFF_MMH_SHAPE_POSITION                                              = 6061, // Shape Position | Shape Position
GFF_MMH_SHAPE_COLLISION_MASK_BITFLAGS                               = 6062, // Shape Collision Mask Bitflags | Shape Collision Mask Bitflags
GFF_MMH_SHAPE_COLLISION_MASK_ALL                                    = 6063, // Shape Collision Mask All flag | Shape Collision Mask All flag
GFF_MMH_SHAPE_COLLISION_MASK_NONE                                   = 6064, // Shape Collision Mask None flag | Shape Collision Mask None flag
GFF_MMH_SHAPE_COLLISION_MASK_ITEMS                                  = 6065, // Shape Collision Mask Items flag | Shape Collision Mask Items flag
GFF_MMH_SHAPE_COLLISION_MASK_CREATURES                              = 6066, // Shape Collision Mask Creatures flag | Shape Collision Mask Creatures flag
GFF_MMH_SHAPE_COLLISION_MASK_PLACEABLES                             = 6067, // Shape Collision Mask Placeables flag | Shape Collision Mask Placeables flag
GFF_MMH_SHAPE_COLLISION_MASK_TRIGGERS                               = 6068, // Shape Collision Mask Triggers flag | Shape Collision Mask Triggers flag
GFF_MMH_SHAPE_COLLISION_MASK_STATIC_GEOMETRY                        = 6069, // Shape Collision Mask Static Geometry flag | Shape Collision Mask Static Geometry flag
GFF_MMH_SHAPE_COLLISION_MASK_NONWALKABLE                            = 6070, // Shape Collision Mask Non-Walkable flag | Shape Collision Mask Non-Walkable flag  
GFF_MMH_SHAPE_BOX_DIM                                               = 6071, // Shape Box Dim | Shape Box Dim
GFF_MMH_SHAPE_RADIUS                                                = 6072, // Shape Radius | Shape Radius
GFF_MMH_SHAPE_HEIGHT                                                = 6073, // Shape Height | Shape Height
GFF_MMH_SHAPE_MESH_SHAPE_FLAGS                                      = 6074, // Mesh Shape Flags | Mesh Shape Flags
GFF_MMH_SHAPE_MESH_HEIGHT_FIELD_AXIS                                = 6075, // Mesh Height Field Axis | Mesh Height Field Axis
GFF_MMH_SHAPE_MESH_HEIGHT_FIELD_EXTENT                              = 6076, // Mesh Height Field Extent | Mesh Height Field Extent
GFF_MMH_SHAPE_COOKED_DATA_STREAM                                    = 6077, // Binary Cooked Data Stream | Binary Cooked Data Stream
GFF_MMH_JOINT_TARGET                                                = 6078, // Joint Target | Joint Target
GFF_MMH_JOINT_TYPE                                                  = 6079, // Joint Type | Joint Type
GFF_MMH_JOINT_TYPE_STRUCT                                           = 6080, // Joint Joint Type | Joint Joint Type
GFF_MMH_JOINT_LOCAL_NORMAL_1                                        = 6081, // Joint Local Normal 1 | Joint Local Normal 1
GFF_MMH_JOINT_LOCAL_NORMAL_2                                        = 6082, // Joint Local Normal 2 | Joint Local Normal 2
GFF_MMH_JOINT_LOCAL_ANCHOR_1                                        = 6083, // Joint Local Anchor 1 | Joint Local Anchor 1
GFF_MMH_JOINT_LOCAL_ANCHOR_2                                        = 6084, // Joint Local Anchor 2 | Joint Local Anchor 2
GFF_MMH_JOINT_LOCAL_AXIS_1                                          = 6085, // Joint Local Axis 1 | Joint Local Axis 1
GFF_MMH_JOINT_LOCAL_AXIS_2                                          = 6086, // Joint Local Axis 2 | Joint Local Axis 2
GFF_MMH_JOINT_MAX_FORCE                                             = 6087, // Joint Max Force | Joint Max Force
GFF_MMH_JOINT_MAX_TORQUE                                            = 6088, // Joint Max Torque | Joint Max Torque
GFF_MMH_JOINT_COLLISION_ENABLED                                     = 6089, // Joint Collision Enabled | Joint Collision Enabled
GFF_MMH_JOINT_SPHERICAL_SWING_AXIS                                  = 6090, // Spherical Swing Axis | Spherical Swing Axis
GFF_MMH_JOINT_SPHERICAL_PROJECTION_DISTANCE                         = 6091, // Spherical Projection Distance | Spherical Projection Distance
GFF_MMH_JOINT_SPHERICAL_TWIST_LIMIT_LOW                             = 6092, // Spherical Twist Limit Low | Spherical Twist Limit Low
GFF_MMH_JOINT_SPHERICAL_TWIST_LIMIT_HIGH                            = 6093, // Spherical Twist Limit High | Spherical Twist Limit High
GFF_MMH_JOINT_SPHERICAL_SWING_LIMIT                                 = 6094, // Spherical Swing Limit | Spherical Swing Limit
GFF_MMH_JOINT_SPHERICAL_TWIST_SWING                                 = 6095, // Spherical Twist Spring | Spherical Twist Spring
GFF_MMH_JOINT_SPHERICAL_SWING_SPRING                                = 6096, // Spherical Swing Spring | Spherical Swing Spring
GFF_MMH_JOINT_SPHERICAL_JOINT_SPRING                                = 6097, // Spherical Joint Spring | Spherical Joint Spring
GFF_MMH_JOINT_SPHERICAL_PROJECTION_MODE                             = 6098, // Spherical Projection Mode | Spherical Projection Mode
GFF_MMH_JOINT_SPHERICAL_SPHERE_FLAGS                                = 6099, // Spherical Sphere Flags | Spherical Sphere Flags
GFF_MMH_JOINT_REVOLUTE_LIMIT_LOW                                    = 6100, // Revolute Limit Low | Revolute Limit Low
GFF_MMH_JOINT_REVOLUTE_LIMIT_HIGH                                   = 6101, // Revolute Limit High | Revolute Limit High
GFF_MMH_JOINT_REVOLUTE_PROJECTION_DISTANCE                          = 6102, // Revolute Projection Distance | Revolute Projection Distance
GFF_MMH_JOINT_REVOLUTE_PROJECTION_ANGLE                             = 6103, // Revolute Projection Angle | Revolute Projection Angle
GFF_MMH_JOINT_REVOLUTE_PROJECTION_MODE                              = 6104, // Revolute Projection Mode | Revolute Projection Mode
GFF_MMH_JOINT_REVOLUTE_SPRING                                       = 6105, // Revolute Spring | Revolute Spring
GFF_MMH_JOINT_REVOLUTE_MOTOR_VEL_TARGET                             = 6106, // Revolute Motor Velocity Target | Revolute Motor Velocity Target
GFF_MMH_JOINT_REVOLUTE_MOTOR_MAX_FORCE                              = 6107, // Revolute Max Force | Revolute Max Force
GFF_MMH_JOINT_REVOLUTE_MOTOR_FREE_SPIN                              = 6108, // Revolute Free Spin | Revolute Free Spin
GFF_MMH_JOINT_REVOLUTE_REVOLUTE_FLAGS                               = 6109, // Revolute Flags | Revolute Flags
GFF_MMH_JOINT_DISTANCE_MIN_DISTANCE                                 = 6110, // Distance Min Distance | Distance Min Distance
GFF_MMH_JOINT_DISTANCE_MAX_DISTANCE                                 = 6111, // Distance Max Distance | Distance Max Distance
GFF_MMH_JOINT_DISTANCE_SPRING                                       = 6112, // Distance Spring | Distance Spring
GFF_MMH_JOINT_DISTANCE_DISTANCE_FLAGS                               = 6113, // Distance Flags | Distance Flags
GFF_MMH_JOINT_PULLEY_PULLEY_1                                       = 6114, // Pulley 1 | Pulley 1
GFF_MMH_JOINT_PULLEY_PULLEY_2                                       = 6115, // Pulley 2 | Pulley 2
GFF_MMH_JOINT_PULLEY_DISTANCE                                       = 6116, // Pulley Distance | Pulley Distance
GFF_MMH_JOINT_PULLEY_STIFFNESS                                      = 6117, // Pulley Stiffness | Pulley Stiffness
GFF_MMH_JOINT_PULLEY_RATIO                                          = 6118, // Pulley Ratio | Pulley Ratio
GFF_MMH_JOINT_PULLEY_MOTOR_VEL_TARGET                               = 6119, // Pulley Motor Velocity Target | Pulley Motor Velocity Target
GFF_MMH_JOINT_PULLEY_MOTOR_MAX_FORCE                                = 6120, // Pulley Motor Max Force | Pulley Motor Max Force
GFF_MMH_JOINT_PULLEY_MOTOR_FREE_SPIN                                = 6121, // Pulley Motor Free Spin | Pulley Motor Free Spin
GFF_MMH_JOINT_PULLEY_PULLEY_FLAGS                                   = 6122, // Pulley Flags | Pulley Flags
GFF_MMH_JOINT_6DOF_X_MOTION                                         = 6123, // 6DOF X Motion | 6DOF X Motion
GFF_MMH_JOINT_6DOF_Y_MOTION                                         = 6124, // 6DOF Y Motion | 6DOF Y Motion
GFF_MMH_JOINT_6DOF_Z_MOTION                                         = 6125, // 6DOF Z Motion | 6DOF Z Motion
GFF_MMH_JOINT_6DOF_SWING_1_MOTION                                   = 6126, // 6DOF Swing 1 Motion | 6DOF Swing 1 Motion
GFF_MMH_JOINT_6DOF_SWING_2_MOTION                                   = 6127, // 6DOF Swing 2 Motion | 6DOF Swing 2 Motion
GFF_MMH_JOINT_6DOF_TWIST_MOTION                                     = 6128, // 6DOF Twist Motion | 6DOF Twist Motion
GFF_MMH_JOINT_6DOF_LINEAR_LIMIT                                     = 6129, // 6DOF Linear Limit | 6DOF Linear Limit
GFF_MMH_JOINT_6DOF_SWING_1_LIMIT                                    = 6130, // 6DOF Swing 1 Limit | 6DOF Swing 1 Limit
GFF_MMH_JOINT_6DOF_SWING_2_LIMIT                                    = 6131, // 6DOF Swing 2 Limit | 6DOF Swing 2 Limit
GFF_MMH_JOINT_6DOF_TWIST_LIMIT_LOW                                  = 6132, // 6DOF Twist Limit Low | 6DOF Twist Limit Low
GFF_MMH_JOINT_6DOF_TWIST_LIMIT_HIGH                                 = 6133, // 6DOF Twist Limit High | 6DOF Twist Limit High
GFF_MMH_JOINT_6DOF_DRIVE_ORIENTATION                                = 6134, // 6DOF Drive Orientation | 6DOF Drive Orientation
GFF_MMH_JOINT_6DOF_DRIVE_X_DRIVE_TYPE                               = 6135, // 6DOF Drive X Drive Type | 6DOF Drive X Drive Type
GFF_MMH_JOINT_6DOF_DRIVE_X_DRIVE_SPRING                             = 6136, // 6DOF Drive X Drive Spring | 6DOF Drive X Drive Spring
GFF_MMH_JOINT_6DOF_DRIVE_X_DRIVE_DAMPING                            = 6137, // 6DOF Drive X Drive Damping | 6DOF Drive X Drive Damping
GFF_MMH_JOINT_6DOF_DRIVE_X_DRIVE_FORCE_LIMIT                        = 6138, // 6DOF Drive X Drive Force Limit | 6DOF Drive X Drive Force Limit
GFF_MMH_JOINT_6DOF_DRIVE_Y_DRIVE_TYPE                               = 6139, // 6DOF Drive Y Drive Type | 6DOF Drive Y Drive Type
GFF_MMH_JOINT_6DOF_DRIVE_Y_DRIVE_SPRING                             = 6140, // 6DOF Drive Y Drive Spring | 6DOF Drive Y Drive Spring
GFF_MMH_JOINT_6DOF_DRIVE_Y_DRIVE_DAMPING                            = 6141, // 6DOF Drive Y Drive Damping | 6DOF Drive Y Drive Damping
GFF_MMH_JOINT_6DOF_DRIVE_Y_DRIVE_FORCE_LIMIT                        = 6142, // 6DOF Drive Y Drive Force Limit | 6DOF Drive Y Drive Force Limit
GFF_MMH_JOINT_6DOF_DRIVE_Z_DRIVE_TYPE                               = 6143, // 6DOF Drive Z Drive Type | 6DOF Drive Z Drive Type
GFF_MMH_JOINT_6DOF_DRIVE_Z_DRIVE_SPRING                             = 6144, // 6DOF Drive Z Drive Spring | 6DOF Drive Z Drive Spring
GFF_MMH_JOINT_6DOF_DRIVE_Z_DRIVE_DAMPING                            = 6145, // 6DOF Drive Z Drive Damping | 6DOF Drive Z Drive Damping
GFF_MMH_JOINT_6DOF_DRIVE_Z_DRIVE_FORCE_LIMIT                        = 6146, // 6DOF Drive Z Drive Force Limit | 6DOF Drive Z Drive Force Limit
GFF_MMH_JOINT_6DOF_DRIVE_SWING_DRIVE_TYPE                           = 6147, // 6DOF Drive Swing Drive Type | 6DOF Drive Swing Drive Type
GFF_MMH_JOINT_6DOF_DRIVE_SWING_DRIVE_SPRING                         = 6148, // 6DOF Drive Swing Drive Spring | 6DOF Drive Swing Drive Spring
GFF_MMH_JOINT_6DOF_DRIVE_SWING_DRIVE_DAMPING                        = 6149, // 6DOF Drive Swing Drive Damping | 6DOF Drive Swing Drive Damping
GFF_MMH_JOINT_6DOF_DRIVE_SWING_DRIVE_FORCE_LIMIT                    = 6150, // 6DOF Drive Swing Drive Force Limit | 6DOF Drive Swing Drive Force Limit
GFF_MMH_JOINT_6DOF_DRIVE_TWIST_DRIVE_TYPE                           = 6151, // 6DOF Drive Twist Drive Type | 6DOF Drive Twist Drive Type
GFF_MMH_JOINT_6DOF_DRIVE_TWIST_DRIVE_SPRING                         = 6152, // 6DOF Drive Twist Drive Spring | 6DOF Drive Twist Drive Spring
GFF_MMH_JOINT_6DOF_DRIVE_TWIST_DRIVE_DAMPING                        = 6153, // 6DOF Drive Twist Drive Damping | 6DOF Drive Twist Drive Damping
GFF_MMH_JOINT_6DOF_DRIVE_TWIST_DRIVE_FORCE_LIMIT                    = 6154, // 6DOF Drive Twist Drive Force Limit | 6DOF Drive Twist Drive Force Limit
GFF_MMH_JOINT_6DOF_DRIVE_SLERP_DRIVE_TYPE                           = 6155, // 6DOF Drive Slerp Drive Type | 6DOF Drive Slerp Drive Type
GFF_MMH_JOINT_6DOF_DRIVE_SLERP_DRIVE_SPRING                         = 6156, // 6DOF Drive Slerp Drive Spring | 6DOF Drive Slerp Drive Spring
GFF_MMH_JOINT_6DOF_DRIVE_SLERP_DRIVE_DAMPING                        = 6157, // 6DOF Drive Slerp Drive Damping | 6DOF Drive Slerp Drive Damping
GFF_MMH_JOINT_6DOF_DRIVE_SLERP_DRIVE_FORCE_LIMIT                    = 6158, // 6DOF Drive Slerp Drive Force Limit | 6DOF Drive Slerp Drive Force Limit
GFF_MMH_JOINT_6DOF_DRIVE_POSITION                                   = 6159, // 6DOF Drive Position | 6DOF Drive Position
GFF_MMH_JOINT_6DOF_DRIVE_LINEAR_VELOCITY                            = 6160, // 6DOF Drive Linear Velocity | 6DOF Drive Linear Velocity
GFF_MMH_JOINT_6DOF_DRIVE_ANGULAR_VELOCITY                           = 6161, // 6DOF Drive Angular Velocity | 6DOF Drive Angular Velocity
GFF_MMH_JOINT_6DOF_PROJECTION_DISTANCE                              = 6162, // 6DOF Drive Projection Distance | 6DOF Drive Projection Distance
GFF_MMH_JOINT_6DOF_PROJECTION_ANGLE                                 = 6163, // 6DOF Drive Projection Angle | 6DOF Drive Projection Angle
GFF_MMH_JOINT_6DOF_GEAR_RATIO                                       = 6164, // 6DOF Gear Ratio | 6DOF Gear Ratio
GFF_MMH_JOINT_6DOF_PROJECTION_MODE                                  = 6165, // 6DOF Projection Mode | 6DOF Projection Mode
GFF_MMH_JOINT_6DOF_D6_FLAGS                                         = 6166, // 6DOF D6 Flags | 6DOF D6 Flags
GFF_MMH_DATA_SEMANTIC                                               = 6167, // Data Semantic | Data Semantic
GFF_MMH_DATA_IS_INDEX_STREAM                                        = 6168, // Data Is Index Stream | Data Is Index Stream
GFF_MMH_DATA_TYPE                                                   = 6169, // Data Type/Index Type | Data Type/Index Type
GFF_MMH_DATA_BITFLAGS                                               = 6170, // Data Bitflags | Data Bitflags
GFF_MMH_DATA_LOOPING                                                = 6171, // Data Data Looping flag | Data Data Looping flag
GFF_MMH_DATA_INSTANCED                                              = 6172, // Data Instanced flag | Data Instanced flag
GFF_MMH_DATA_COUNT                                                  = 6173, // Data Count | Data Count
GFF_MMH_DATA_PRIMITIVE_TYPE                                         = 6174, // Data Primitive Type | Data Primitive Type
GFF_MMH_DATA_FREQUENCY                                              = 6175, // Data Frequency | Data Frequency
GFF_MMH_MESH_CAST_RUNTIME_SHADOW                                    = 6176, // Runtime Shadow Casting | Runtime Shadow Casting
GFF_MMH_MESH_CAST_BAKED_SHADOW                                      = 6177, // Cast Baked Shadow | Cast Baked Shadow
GFF_MMH_SHAPE_COLLISION_MASK_EFFECTS								= 6178, // Shape Collision Mask Effects
GFF_MMH_SHAPE_COLLISION_MASK_WAYPOINTS								= 6179, // Shape Collision Mask Waypoints
GFF_MMH_FLIPBOOK_FRAMES_PER_SECOND                                  = 6180, // Flipbook FPS | Flipbook FPS
GFF_MMH_FLIPBOOK_ROWS                                               = 6181, // Flipbook Rows | Flipbook Rows
GFF_MMH_FLIPBOOK_COLUMNS                                            = 6182, // Flipbook Columns | Flipbook Columns
GFF_MMH_FLIPBOOK_RANDOM_START_FRAME                                 = 6183, // Flipbook Random Start Frame | Flipbook Random Start Frame
GFF_MMH_EMITTER_TARGET_NAME                                         = 6184, // Emitter Target Name | Emitter Target Name
GFF_MMH_EMITTER_TARGET_ATTRACTION                                   = 6185, // Emitter Target Attraction | Emitter Target Attraction
GFF_MMH_EMITTER_TARGET_RADIUS                                       = 6186, // Emitter Target Radius | Emitter Target Radius
GFF_MMH_EMITTER_SPAWN_DIRECTION_TRACKS_TARGET                       = 6187, // Emitter Spawn Direction Tracks Target | Emitter Spawn Direction Tracks Target
GFF_MMH_EMITTER_KILL_PARTICLE_WHEN_TARGET_HIT                       = 6188, // Emitter Kill Particle When Hit | Emitter Kill Particle When Hit
GFF_MMH_EMITTER_FLIPBOOK_TYPE                                       = 6189, // Emitter flipbook type
GFF_MMH_LIGHTPROBE_IRRADIANCE_COEFFICIENTS_RED                      = 6190, // Light probe | red component of compressed irradiance coefficients
GFF_MMH_LIGHTPROBE_IRRADIANCE_COEFFICIENTS_GREEN                    = 6191, // Light probe | green component of compressed irradiance coefficients
GFF_MMH_LIGHTPROBE_IRRADIANCE_COEFFICIENTS_BLUE                     = 6192, // Light probe | blue component of compressed irradiance coefficients
GFF_MMH_MESH_CUT_AWAY												= 6193, // Cut Away | Cut Away
GFF_MMH_MESH_PUNCH_THROUGH											= 6194, // Punch Through | Punch Through
GFF_MMH_CLOTH_THICKNESS                                             = 6195, // Cloth thickness | Cloth thickness
GFF_MMH_CLOTH_DENSITY                                               = 6196, // Cloth density | Cloth density
GFF_MMH_CLOTH_BENDING_STIFFNESS                                     = 6197, // Cloth bending stiffness | Cloth bending stiffness
GFF_MMH_CLOTH_STRETCHING_STIFFNESS                                  = 6198, // Cloth stretching stiffness | Cloth stretching stiffness
GFF_MMH_CLOTH_DAMPING_COEFFICIENT                                   = 6199, // Cloth damping coefficient | Cloth damping coefficient
GFF_MMH_CLOTH_FRICTION                                              = 6200, // Cloth friction | Cloth friction
GFF_MMH_CLOTH_PRESSURE                                              = 6201, // Cloth pressure | Cloth pressure
GFF_MMH_CLOTH_TEAR_FACTOR                                           = 6202, // Cloth tear factor | Cloth tear factor
GFF_MMH_CLOTH_COLLISION_RESPONSE_COEFFICIENT                        = 6203, // Cloth collisions response coefficient | Cloth collisions response coefficient
GFF_MMH_CLOTH_ATTACHMENT_RESPONSE_COEFFICIENT                       = 6204, // Cloth attachment response coefficient | Cloth attachment response coefficient
GFF_MMH_CLOTH_ATTACHMENT_TEAR_FACTOR                                = 6205, // Cloth attachment tear factor | Cloth attachment tear factor
GFF_MMH_CLOTH_SOLVER_ITERATIONS                                     = 6206, // Cloth solver iterations | Cloth solver iterations
GFF_MMH_CLOTH_EXTERNAL_ACCELERATION                                 = 6207, // Cloth external acceleration | Cloth external acceleration
GFF_MMH_CLOTH_WAKE_UP_COUNTER                                       = 6208, // Cloth wake up counter | Cloth wake up counter
GFF_MMH_CLOTH_SLEEP_LINEAR_VELOCITY                                 = 6209, // Cloth sleep linear velocity | Cloth sleep linear velocity
GFF_MMH_CLOTH_FLAG_BITFLAGS                                         = 6210, // Cloth flag bitflags | Cloth flag bitflags
GFF_MMH_CLOTH_FLAG_PRESSURE                                         = 6211, // Cloth flag pressure | Cloth flag pressure
GFF_MMH_CLOTH_FLAG_STATIC                                           = 6212, // Cloth flag static | Cloth flag static
GFF_MMH_CLOTH_FLAG_DISABLE_COLLISION                                = 6213, // Cloth flag disable collision | Cloth flag disable collision
GFF_MMH_CLOTH_FLAG_SELFCOLLISION                                    = 6214, // Cloth flag self collision | Cloth flag self collision
GFF_MMH_CLOTH_FLAG_VISUALIZATION                                    = 6215, // Cloth flag visualization | Cloth flag visualization
GFF_MMH_CLOTH_FLAG_GRAVITY                                          = 6216, // Cloth flag gravity | Cloth flag gravity
GFF_MMH_CLOTH_FLAG_BENDING                                          = 6217, // Cloth flag bending | Cloth flag bending
GFF_MMH_CLOTH_FLAG_BENDING_ORTHO                                    = 6218, // Cloth flag bending ortho | Cloth flag bending ortho
GFF_MMH_CLOTH_FLAG_DAMPING                                          = 6219, // Cloth flag damping | Cloth flag damping
GFF_MMH_CLOTH_FLAG_COLLISION_TWOWAY                                 = 6220, // Cloth flag collision two way | Cloth flag collision two way
GFF_MMH_CLOTH_FLAG_TRIANGLE_COLLISION                               = 6221, // Cloth flag triangle collision | Cloth flag triangle collision
GFF_MMH_CLOTH_FLAG_TEARABLE                                         = 6222, // Cloth flag tearable | Cloth flag tearable
GFF_MMH_CLOTH_FLAG_HARDWARE                                         = 6223, // Cloth flag hardware | Cloth flag hardware
GFF_MMH_CLOTH_FLAG_COMDAMPING                                       = 6224, // Cloth flag COM damping | Cloth flag COM damping
GFF_MMH_CLOTH_ATTACHMENT_TYPE                                       = 6225, // Cloth attachment type | Cloth attachment type
GFF_MMH_CLOTH_ATTACHMENT_FLAG_BITFLAGS                              = 6226, // Cloth attachment flag bitflags | Cloth attachment flag bitflags
GFF_MMH_CLOTH_ATTACHMENT_FLAG_TWO_WAY_ATTACHMENT                    = 6227, // Cloth attachment flag two way attachment | Cloth attachment flag two way attachment
GFF_MMH_CLOTH_ATTACHMENT_FLAG_TEARABLE_ATTACHMENT                   = 6228, // Cloth attachment flag tearable attachment | Cloth attachment flag tearable attachment
GFF_MMH_CLOTH_ATTACHMENT_SHAPE_NAME                                 = 6229, // Cloth attachment shape name | Cloth attachment shape name
GFF_MMH_CLOTH_ATTACHMENT_VERTEX_ID                                  = 6230, // Cloth attachment vertex id | Cloth attachment vertex id
GFF_MMH_CLOTH_ATTACHMENT_LOCAL_POS                                  = 6231, // Cloth attachment local pos | Cloth attachment local pos
GFF_MMH_CLOTH_COOKED_DATA_STREAM                                    = 6232, // Binary Cooked Data Stream | Binary Cooked Data Stream
GFF_MMH_CLOTH_MESH_GROUP_STRUCT                                     = 6233, // Mesh Group for Cloth | Mesh Group for Cloth
GFF_MMH_NODE_EMITTER_TYPE                                           = 6234, // Emitter type | Emitter type 
GFF_MMH_NODE_CRUST_HOOK_ID                                          = 6235, // Hook ID | Hook ID
GFF_MMH_COLLISION_OBJECT_VOLUME                                     = 6236, // DEPRECATED
GFF_MMH_OBJECT_VOLUME                                               = 6237, // DEPRECATED
GFF_MMH_EXPORT_TAG_VARIABLE_TYPE                                    = 6238, // Exported Tag Type | Exported Tag Type
GFF_MMH_EMITTER_IS_PHYSICS_EMITTER                                  = 6239, // Is Physics Emitter | Is Physics Emitter
GFF_MMH_SHAPE_VOLUME                                                = 6240, // Physics Shape Volume | Physics Shape Volume
GFF_MMH_SHAPE_NAME                                                  = 6241, // Shape Name | Shape Name
GFF_MMH_SNAP_POSITION                                               = 6242, // Snap Position | Vector3 position of a snap point
GFF_MMH_EMITTER_IS_PHYSICS_OBJECT_SPAWN_EMITTER                     = 6243, // Is Physics Object Spawn Emitter | Is Physics Object Spawn Emitter
GFF_MMH_SHAPE_ALLOW_EMITTER_SPAWN                                   = 6244, // Allow Emitter Spawn | Allow Emitter Spawn
GFF_MMH_COLLISION_GROUP                                             = 6245, // Collision Group | Collision Group
GFF_MMH_EMITTER_EMITTER_ATTACHMENT_TYPE                             = 6246, // Emitter Attachment Type | Emitter Attachment Type
GFF_MMH_EMITTER_EMITTER_ATTACHMENT_NAME                             = 6247, // Emitter Attachment Name | Emitter Attachment Name
GFF_MMH_FACIAL_ANIMATION_BLUEPRINT_NAME                             = 6248, // Facial Animation Type | Facial Animation Blueprint Name

GFF_MMH_NODE_POINT_LIGHT_INTENSITY_VARIATION                        = 6249, // Point Light Intensity Variation | Point Light Intensity Variation for flickering lights
GFF_MMH_NODE_POINT_LIGHT_INTENSITY_PERIOD                           = 6250, // Point Light Intensity Period | Point Light Intensity Period for flickering lights
GFF_MMH_NODE_POINT_LIGHT_INTENSITY_PERIOD_DELTA                     = 6251, // Point Light Intensity Period delta | Point Light Intensity Period delta for flickering lights
GFF_MMH_SHAPE_FADEABLE                                              = 6252, // Fadeable physics part 

GFF_MMH_LIGHTPROBE_IRRADIANCE_RES                                   = 6253, // Light probe | resource name for MTX file for irradiance coefficients

GFF_MMH_BONE_INDEX                                                  = 6254, // Bone index | Index of this bone into the object's bone array
GFF_MMH_MESH_BONES_USED                                             = 6255, // Bones used | List of bones used by this mesh (if it is skinned)
GFF_MMH_TOTAL_BONES                                                 = 6256, // Total bones | The total number of bones with a valid index in the mmh.

GFF_MMH_CLOTH_WIND_ENABLED                                          = 6257, // TRUE if Wind enabled for cloth
GFF_MMH_CLOTH_WIND_SPACE                                            = 6258, // World or local space of wind direction
GFF_MMH_CLOTH_WIND_DIRECTION                                        = 6259, // Wind direction for cloth
GFF_MMH_CLOTH_WIND_RESPONSE                                         = 6260, // The response of the cloth on wind per second
GFF_MMH_CLOTH_WIND_RESPONSE_LIMIT                                   = 6261, // The maximum response of the cloth on wind per frame
CFF_MMH_CLOTH_WIND_STRENGTH                                         = 6262, // The wind strength
GFF_MMH_CLOTH_WIND_GUST_MIN_STRENGTH                                = 6263, // The gusting min strength
GFF_MMH_CLOTH_WIND_GUST_MAX_STRENGTH                                = 6264, // The gusting max strength
GFF_MMH_CLOTH_WIND_GUST_MIN_DURATION                                = 6265, // The gusting min duration
GFF_MMH_CLOTH_WIND_GUST_MAX_DURATION                                = 6266, // The gusting max strength
GFF_MMH_CLOTH_WIND_GUST_MIN_INTERVAL                                = 6267, // The minimum interval between two gusts
GFF_MMH_CLOTH_WIND_GUST_MAX_INTERVAL                                = 6268, // The maximum interval between two gusts
GFF_MMH_CLOTH_WIND_GUST_DIR_CHANGE                                  = 6269, // The parameter which shows how big is difference between wind and gusting direction
CFF_MMH_CLOTH_WIND_GUST_AXIS_RATIO                                  = 6270, // The parameter defines ratio of each axis component for gusting wind changes
GFF_MMH_CLOTH_WIND_SPEEDTREE_UPDATE_TIME                            = 6271, // The refresh time for parameters which shared with speedtree
GFF_MMH_CLOTH_WIND_SPEEDTREE_STRENGTH                               = 6272, // TRUE if speedtree wind strength used like wind strength multiplier
GFF_MMH_CLOTH_WIND_SPEEDTREE_DIRECTION                              = 6273, // TRUE if speedtree wind direction overrides cloth wind direction

GFF_MMH_EXPORT_CONTROLLER_INDEX                                     = 6274, // Export Controller Index| Index of this controller in the controller array (they are sorted by name)
GFF_MMH_TOTAL_EXPORTS                                               = 6275, // Number of exports | Number of controllers exported (for animation) on this model.

GFF_MMH_CLOTH_WIND_SPEEDTREE_PARAMS                                 = 6276, // TRUE if parameters for cloth wind is taken from speedtree wind system.

GFF_MMH_SHAPE_COLLISION_MASK_WATER                                  = 6277, // Shape group flag

GFF_MMH_SCALE                                                       = 6278, // Scale of object node

GFF_MMH_NODE_EMITTER_AGEMAP_COLOR_MULTIPLIER                        = 6279,
GFF_MMH_NODE_EMITTER_AGEMAP_SCALEX_MULTIPLIER                       = 6280,
GFF_MMH_NODE_EMITTER_AGEMAP_SCALEY_MULTIPLIER                       = 6281,

GFF_MMH_NODE_EMITTER_OPTIONS_BOUNCINESS                             = 6282,
GFF_MMH_NODE_EMITTER_OPTIONS_FRICTION                               = 6283,
GFF_MMH_NODE_EMITTER_MESH_PARTICLE_MODELNAME                        = 6284,
GFF_MMH_NODE_SPAWN_VOLUME_TYPE                                      = 6285, // type of spawn volume to use
GFF_MMH_NODE_SPAWN_VOLUME_RADIUS                                    = 6286, // procedural spawn volume radius
GFF_MMH_NODE_SPAWN_VOLUME_CYLINDER_LENGTH                           = 6287, 
GFF_MMH_NODE_SPAWN_VOLUME_CYLINDER_AXIS                             = 6288,
GFF_MMH_NODE_SPAWN_VOLUME_BOX_MIN                                   = 6289,
GFF_MMH_NODE_SPAWN_VOLUME_BOX_MAX                                   = 6290,
GFF_MMH_NODE_SPAWN_VOLUME_OPTIONS_NORMALS_AS_DIRECTION              = 6291, // use the spawnvolume normals as directions for particles

GFF_MMH_WEAPONTRAIL_SEGMENT_LENGTH                                  = 6292, // Weapon trail size | The length of the segment that generates a weapon trail
GFF_MMH_WEAPONTRAIL_DURATION                                        = 6293, // Weapon trail duration | The amount of time before the trail ends

GFF_MMH_NODE_EMITTER_WORLD_AXIS_ACCELERATION                        = 6294, // independent world axis acceleration for particles

GFF_MMH_SHAPE_COLLISION_MASK_TERRAIN_WALL                           = 6295, // Shape group flag

GFF_MMH_NODE_LIGHT_AFFECT_DOMAIN                                    = 6296, // Analogous to the GFF_LIGHT_AFFECT_DOMAIN tag, as it is read from an mmh file.
GFF_MMN_NODE_EMITTER_VERTEX_FORMAT                                  = 6297, // vertex format for emitters

GFF_MMH_NODE_EMITTER_OPTIONS_OBJECT_SPACE_ACCELERATION              = 6298, // additional acceleration (m_vWorldAxisAcceleration) is actually in object space
GFF_MMH_NODE_EMITTER_INITIAL_ROTATION                               = 6299, // particle initial rotation value
GFF_MMH_NODE_EMITTER_INITIAL_ROTATION_RANGE                         = 6300, // particle initial rotation range

GFF_MMH_MESH_RECEIVE_BAKED_SHADOW                                   = 6301, // Receive Shadow | Receive Shadow

GFF_MMH_NODE_EMITTER_MESH_PARTICLE_UP_AXIS                          = 6302,
GFF_MMH_NODE_EMITTER_MESH_PARTICLE_ROLL_AXIS                        = 6303,

GFF_MMH_MESH_RECEIVE_RUNTIME_SHADOW                                 = 6304, // Receive Shadow | Receive Shadow
GFF_MMH_SHAPE_COLLISION_MASK_WALKABLE                               = 6305, // Walkable flag

GFF_MMH_MODEL_MESH_NAME_LIST                                        = 6306, // list of referenced meshes
GFF_MMH_NODE_MESH_NAME                                              = 6307, // which referenced mesh to look in 
GFF_MMH_NODE_EMITTER_UV_DISTRIBUTION_SIZE                           = 6308, // number of particles to spread texture over
GFF_MMH_NODE_EMITTER_IGNORE_DISTORTION                              = 6309, // render after distortion effects

GFF_MMH_NODE_EMITTER_SPLATPARAMS_WIDTH                              = 6310,
GFF_MMH_NODE_EMITTER_SPLATPARAMS_HEIGHT                             = 6311,
GFF_MMH_NODE_EMITTER_SPLATPARAMS_NUMSAMPLES_WIDTH                   = 6312,
GFF_MMH_NODE_EMITTER_SPLATPARAMS_NUMSAMPLES_HEIGHT                  = 6313,
GFF_MMH_NODE_EMITTER_SPLATPARAMS_ORIENTATION_RANGE                  = 6314,
GFF_MMH_NODE_EMITTER_SPLATPARAMS_LIFE                               = 6315,
GFF_MMH_NODE_EMITTER_SPLATPARAMS_FLIPBOOK_TYPE                      = 6316,
GFF_MMH_NODE_EMITTER_SPLATPARAMS_FLIPBOOK_FRAMES_PER_SECOND         = 6317,
GFF_MMH_NODE_EMITTER_SPLATPARAMS_FLIPBOOK_ROWS                      = 6318,
GFF_MMH_NODE_EMITTER_SPLATPARAMS_FLIPBOOK_COLUMNS                   = 6319,
GFF_MMH_NODE_EMITTER_SPLATPARAMS_FLIPBOOK_RANDOM_START_FRAME        = 6320,
GFF_MMH_NODE_EMITTER_CAN_PARTICLES_SPLAT                            = 6321,
__deprecated__GFF_MMH_NODE_EMITTER_SPLATPARAMS_AGE_MAP_ELEMENT_PERCENT_LIFE_ELAPSED= 6322,
GFF_MMH_NODE_EMITTER_LOD											= 6323,
GFF_MMH_NODE_EMITTER_SPLATPARAMS_MATERIALNAME                       = 6324,

GFF_MMH_NODE_EMITTER_USER_PARAM_NAME                                = 6325,

__deprecated__6326                                                  = 6326,
GFF_MMH_REMOTE_MATERIAL_DECAL_NAME                                  = 6327,
GFF_MMH_REMOTE_MATERIAL_FRESNEL_FALLOFF                             = 6328,
GFF_MMH_REMOTE_MATERIAL_INVERT_FRESNEL                              = 6329,

GFF_MMH_NODE_SOUND_MATERIAL                                         = 6330,

GFF_MMH_REMOTE_MATERIAL_ALPHA                                       = 6331,
GFF_MMH_REMOTE_MATERIAL_TINT                                        = 6332,
GFF_MMH_EMITTER_PRESIMULATE_TIME                                    = 6333,

GFF_MMH_MESH_IS_VFX_MESH                                            = 6334,
GFF_MMH_MESH_MATERIAL_COLOR                                         = 6335,

GFF_MMH_LIGHTPROBE_IRRADIANCE_RED                                   = 6336,
GFF_MMH_LIGHTPROBE_IRRADIANCE_GREEN                                 = 6337,
GFF_MMH_LIGHTPROBE_IRRADIANCE_BLUE                                  = 6338,

GFF_MMH_LIGHT_CAN_BE_OCCLUDED                                       = 6339,    // Can Be Occluded |bool Whether or not light can be occluded at runtime (based on light subsets).

GFF_MMH_USE_VARIATION_TINT                                          = 6340,    // can use designer variation tint color
GFF_MMH_NODE_EMITTER_SPLATPARAMS_HOLD_LAST_FRAME                    = 6341,    // splat particle will stop at the last frame of the contact sheet and not wrap
GFF_MMH_EMITTER_EMITTER_ATTACHMENT_SPAWN_ON_SURFACE                 = 6342,    // spawn particles on surface of physics volume
GFF_MMH_EMITTER_EMITTER_ATTACHMENT_USE_NORMAL_FOR_VELOCITY          = 6343,    // use the normal as velocity direction
GFF_MMH_NODE_EMITTER_SPLATPARAMS_AGEMAP_COLOR_MULTIPLIER            = 6344,    // color multiplier for splat

GFF_MMH_NODE_LIGHT_VERSION                                          = 6345,     // Light Version - for avoiding the messing up of DA1 levels

GFF_MMH_MESH_DEFAULT_HIDDEN                                         = 6346,     // Mesh Default Hidden | Whether this mesh node should be hidden by default.


GFF_MMH_SHAPE_TYPE_STRUCT                                           = 6998, // Shape Type Struct | Generic Struct Reference
GFF_MMH_CHILDREN                                                    = 6999, // Children | Generic Struct Reference List

// MMH GFF range reserved up to 6999

// Begin terrain range
GFF_TERRAIN_VERSION                 =  7000, // Terrain Name | string.  Name of terrain.
GFF_TERRAIN_BASE_ROWS               =  7001, // Base Rows | Number of rows in a sector.
GFF_TERRAIN_BASE_COLUMNS            =  7002, // Base Columns | Number of columns in a sector.
GFF_TERRAIN_LENGTH_UNITS            =  7003, // Length Units | Length of a sector.
GFF_TERRAIN_WIDTH_UNITS             =  7004, // Width Units | Width of a sector.
GFF_TERRAIN_SECTOR_ROWS             =  7005, // Area Rows | Number of row sectors.
GFF_TERRAIN_SECTOR_COLUMNS          =  7006, // Area Columns | Number of column sectors.
GFF_TERRAIN_TESSELLATION            =  7007, // Tessellation | Tessellation level.
GFF_TERRAIN_SECTOR_ID               =  7008, // Sector ID | ID of a sector.
GFF_TERRAIN_SECTOR_LIST             =  7009, // Sector List | List of sectors
GFF_TERRAIN_MESHFACE_ID             =  7010, // Face ID | ID of a face.
GFF_TERRAIN_MESHFACE_LIST           =  7011, // Face List | List of faces.
GFF_TERRAIN_MESHEDGE_ID             =  7012, // Edge ID | ID of an edge.
GFF_TERRAIN_MESHEDGE_START_VERTEX   =  7013, // Edge Start Vertex | Starting vertex for an edge.
//GFF_TERRAIN_MESHEDGE_BOUNDARY_FLAG  =  7014, // Edge Boundary Flag | uint8 (bool) indicating a sector bounding edge.
GFF_TERRAIN_MESHEDGE_SUBEDGE_LIST   =  7015, // Edge Subedge List. | List of subedges for an edge.
GFF_TERRAIN_MESHEDGE_LIST           =  7016, // Edge List | List of edges.
GFF_TERRAIN_SUBEDGE_ID              =  7017, // SubEdge ID | ID of a subedge.
GFF_TERRAIN_MESHVERTEX_ID           =  7018, // Vertex ID | ID of a vertex.
GFF_TERRAIN_MESHVERTEX_POSITION     =  7019, // Vertex Position | vector3 position of a vertex.
GFF_TERRAIN_MESHVERTEX_LEVEL        =  7020, // Vertex Level | int32 level of a vertex.
GFF_TERRAIN_MESHVERTEX_CONSTRAINT_LIST	=  7021, // Vertex Constraint List | List of vertex constraints.
GFF_TERRAIN_MESHVERTEX_CONSTRAINT_ID	=  7022, // Vertex Constraint ID | ID of a vertex constraint.
GFF_TERRAIN_MESHVERTEX_LIST             =  7023, // Vertex List | List of vertices.
GFF_TERRAIN_ELEMENT_ID_VALUE        =  7024, // Element ID Value | Value of the Element ID, unique within a sector.
GFF_TERRAIN_ELEMENT_ID_SECTOR       =  7025, // Element ID Sector | Sector for the Element ID.
GFF_TERRAIN_MATERIAL_VALUE          =  7026, // Material Name | string.  Name of material.
GFF_TERRAIN_MATERIAL_LIST           =  7027, // Material List | List of materials.
GFF_TERRAIN_AREA_INFORMATION        =  7028, // Area Information | Information about the area.
GFF_TERRAIN_VERTEX_U                =  7029, // Vertex U | U texture coordinate of a vertex.
GFF_TERRAIN_VERTEX_V                =  7030, // Vertex V | U texture coordinate of a vertex.
//GFF_TERRAIN_MASK_DATA_WIDTH         =  7031, // [OBSOLETE] Texture mask width | Width of the texture mask.
//GFF_TERRAIN_MASK_DATA_HEIGHT        =  7032, // [OBSOLETE] Texture mask height | Height of the texture mask.
//GFF_TERRAIN_MASK_DATA_STRIDE        =  7033, // [OBSOLETE] Texture mask stride | Stride of the texture mask.
//GFF_TERRAIN_MASK_DATA_ARRAY         =  7034, // [OBSOLETE] Texture mask pointer | Pointer to the start of texture mask data.
//GFF_TERRAIN_VMASK_DATA              =  7035, // [OBSOLETE] V Mask List | List of mask V coordinates.
//GFF_TERRAIN_AMASK_DATA              =  7036, // [OBSOLETE] A Mask List | List of mask A coordinates.
GFF_TERRAIN_MAPVERTEX_ID            =  7037, // Map Vertex ID | ID of a map vertex.
GFF_TERRAIN_MAPVERTEX_UVW           =  7038, // Map Vertex UVW | vector3 position of a map vertex.
GFF_TERRAIN_MAPVERTEX_LIST          =  7039, // Map Vertex List | List of map vertices.
GFF_TERRAIN_MAPEDGE_ID              =  7040, // Map Edge ID | ID of a map edge.
GFF_TERRAIN_MAPEDGE_START_VERTEX    =  7041, // Map Edge Start Vertex | Starting vertex fo a map edge.
GFF_TERRAIN_MAPEDGE_LIST            =  7042, // Map Edge List | List of map edges.
GFF_TERRAIN_MAPFACE_ID              =  7043, // Map Face ID | ID of a map face.
GFF_TERRAIN_MAPFACE_LAYER           =  7044, // Map Face Layer | Layer of a map face.
GFF_TERRAIN_MAPFACE_LIST            =  7045, // Map Face List | List of map faces.
GFF_TERRAIN_MAPFACE_BLENDPAGE_ID    =  7046, // Map Face BlendPageRef | Lookup for blendpage on a face.
GFF_TERRAIN_BLENDWEIGHT_MATID       =  7047, // Blend Weight | Ordered lookup ID for material
GFF_TERRAIN_BLENDWEIGHT_WEIGHT      =  7048, // [DEPRECATED] Blend Weight | Weight value [0,1] inclusive.
GFF_TERRAIN_BLENDTEXEL_WEIGHTLIST   =  7049, // [DEPRECATED] Blend Weight List | List of blend weights
GFF_TERRAIN_BLENDPAGE_ID            =  7050, // Blend Page | ID of page.
GFF_TERRAIN_BLENDPAGE_WIDTH         =  7051, // Blend Page | Width in texels.
GFF_TERRAIN_BLENDPAGE_HEIGHT        =  7052, // Blend Page | Height in texels.
GFF_TERRAIN_BLENDPAGE_TEXEL_LIST    =  7053, // Blend Page | Texels linear array.
GFF_TERRAIN_BLENDPAGE_LIST          =  7054, // Blend Page List | List of blend pages.
GFF_TERRAIN_MESH                    =  7055, // Mesh | struct "MESH".
GFF_TERRAIN_PALETTE                 =  7056, // Palette | Material palette.
GFF_TERRAIN_BLENDTEXEL_BYTEWEIGHTLIST = 7057, // Blend Weight | Byte weight list
GFF_TERRAIN_MESH_NAME               =  7058, // Mesh Name | Name of mesh.
GFF_TERRAIN_PALETTE_NAME            =  7059, // Palette Name | Name of palette.
GFF_TERRAIN_MATERIAL                =  7060, // Material | Material in palette.
GFF_TERRAIN_MATERIAL_ID             =  7061, // Material Name | ID of a material.
GFF_TERRAIN_MATERIAL_NAME           =  7062, // Material Name | Name of a material.
GFF_TERRAIN_MATERIAL_SCALE          =  7063, // Material Scale | Scale applied to material textures.
GFF_TERRAIN_MATERIAL_DIFFUSE_NAME   =  7064, // Diffuse Name | ResName of a texture.
GFF_TERRAIN_MATERIAL_NORMAL_NAME    =  7065, // Normal Name | ResName of a texture.
GFF_TERRAIN_MATERIAL_SPECUALAR_NAME =  7066, // Specular Name | ResName of a texture.
GFF_TERRAIN_MATERIAL_HEIGHTMAP_NAME =  7067, // Heightmap Name | ResName of a texture.
GFF_TERRAIN_PALETTE_PARALLAX_GLOBAL =  7068, // [DEPRECATED] Parallax multiplier | global multiplier to all parallax values.
GFF_TERRAIN_MATERIAL_RELIEF_SCALE   =  7069, // Parallax Relief scale | Per material relief scaling.
GFF_TERRAIN_BLENDTEXEL_6BYTEWEIGHTLIST = 7070, // Blend Weight | Byte weight list with 6-byte encoding.
GFF_TERRAIN_MESHVERTEX_CONSTRAINT_A	=  7071, // Vertex Constraint #A.
GFF_TERRAIN_MESHVERTEX_CONSTRAINT_B	=  7072, // Vertex Constraint #A.
GFF_TERRAIN_MESHEDGE_SUBEDGE_A      =  7073, // Edge Subedge List. | List of subedges for an edge.
GFF_TERRAIN_MESHEDGE_SUBEDGE_B      =  7074, // Edge Subedge List. | List of subedges for an edge.
GFF_TERRAIN_BLENDTEXEL_ID           =  7075, // Blend texel unique ID.
GFF_TERRAIN_SOUND_DATA              =  7076, // Material sound property | Terrain material sound property
GFF_TERRAIN_MATERIAL_SPECULAR_COLOR =  7077, // Specular Color | Per material specular color.

// Terrain range reserved up to 7899

GFF_WATER_INFORMATION               = 7900,
GFF_WATER_VERSION                   = 7901,
GFF_WATER_ID                        = 7902,
GFF_WATER_VERTEX_LIST               = 7903,
GFF_WATER_VERTEX_POSITION           = 7904,
GFF_WATER_VERTEX_NORMAL             = 7905,
GFF_WATER_VERTEX_UVW                = 7906,
GFF_WATER_VERTEX_COLOR              = 7907,
GFF_WATER_VERTEX_INDEX_LIST         = 7908,

// Water range reserved up to 7999

// Begin mesh range
GFF_MESH_CHUNK_VERTEXSIZE           = 8000, // Vertex Size | The size of each vertex in Bytes
GFF_MESH_CHUNK_VERTEXCOUNT          = 8001, // Vertex Count | The number of vertices in this mesh chunk
GFF_MESH_CHUNK_INDEXCOUNT           = 8002, // Index Count | The number of indices in this mesh chunk
GFF_MESH_CHUNK_PRIMITIVETYPE        = 8003, // Primitive Type | The primitive type 
GFF_MESH_CHUNK_INDEXFORMAT          = 8004, // Index Format | The format of the index (UINT16 or UINT32)
GFF_MESH_CHUNK_BASEVERTEXINDEX       = 8005, // Base Vertex Index | The index into the vertex list at which to start indexing
GFF_MESH_CHUNK_VERTEXOFFSET         = 8006, // Vertex Offset | The offset into the list (plus the base) where this chunk's vertices are
GFF_MESH_CHUNK_MININDEX             = 8007, // Min Index | The lowest index in the list of indices
GFF_MESH_CHUNK_VERTICESREFERENCED   = 8008, // Referenced Vertices | The number of vertices being referenced by index
GFF_MESH_CHUNK_STARTINDEX           = 8009, // Start Index | The which index in the stream is the first index used for this chunk
GFF_MESH_CHUNK_HASINSTGEOM          = 8010, // Has Instance Geometry | This field is true (not zero) if this mesh represents instanced geometry
GFF_MESH_CHUNK_ADDITIONALSTREAMS    = 8011, // Additional Streams | Any other streams are stored in this list
GFF_MESH_STREAM_VERTEXSIZE          = 8012, // Vertex Size | The size of the vertices in the stream
GFF_MESH_STREAM_VERTEXCOUNT         = 8013, // Vertex Count | The number of vertices in the stream
GFF_MESH_STREAM_FREQUENCY           = 8014, // Frequency | The frequency of the stream
GFF_MESH_STREAM_LOOPING             = 8015, // Looping | Whether or not the stream loops
GFF_MESH_STREAM_INSTANCED           = 8016, // Instanced | Whether or not the stream is instanced
GFF_MESH_BOUNDS_BOXMIN              = 8017, // Bounding Box Min | The min point of the bounding box
GFF_MESH_BOUNDS_BOXMAX              = 8018, // Bounding Box Max | The max point of the bounding box
GFF_MESH_BOUNDS_SPHERE              = 8019, // Bounding Sphere | The bounding sphere
GFF_MESH_CHUNK_BOUNDS               = 8020, // Bounds | Holds bounding info
GFF_MESH_CHUNKS                     = 8021, // Chunks | List of chunks for this mesh
GFF_MESH_VERTEXDATA                 = 8022, // Vertex Data | The data that composes the vertex stream for this mesh
GFF_MESH_INDEXDATA                  = 8023, // IndexData | The index data that composes this mesh
GFF_MESH_STREAM_VERTEXDATA          = 8024, // Vertex Data | The vertex data for this stream 
GFF_MESH_CHUNK_VERTEXDECLARATOR     = 8025, // Vertex Declarator | The declarator for the vertex streams in this chunk
GFF_MESH_VERTEXDECLARATOR_STREAM    = 8026, // Stream | Which stream this is using 
GFF_MESH_VERTEXDECLARATOR_OFFSET    = 8027, // Offset | THe offset into the data for this stream
GFF_MESH_VERTEXDECLARATOR_DATATYPE  = 8028, // Data Type | The data type of the attribute being described by this decl
GFF_MESH_VERTEXDECLARATOR_USAGE     = 8029, // Usage | The usage is the semantic meaning of the attribute being described by this decl
GFF_MESH_VERTEXDECLARATOR_USAGEINDEX = 8030, // Usage Index | If there is more than one of the same usage this value describes which one it is
GFF_MESH_VERTEXDECLARATOR_METHOD    = 8031, // Method | A value that exists in DX9 but isn't being used
GFF_MESH_INDEXFORMAT                = 8032, // Index Format | The data format of the indices,
GFF_MESH_INSTANCED_STREAM           = 8033, // Int8 | If the mesh stream data is used for instancing
GFF_MESH_CHUNK_INSTANCES_COUNT      = 8034, // Int32 | Number of instances in a binary mesh chunk

// mesh range reserved up to 8999

// Begin animation composer range
GFF_AC_NODE_NAME                    = 9000, // Blend node name | Blend node name
GFF_AC_EDGE_START_ID                = 9001, // Edge start socket ID | Edge start socket ID
GFF_AC_EDGE_END_ID                  = 9002, // Edge end socket ID | Edge end socket ID
GFF_AC_CAPTION                      = 9003, // Caption | Caption
GFF_AC_NODE_SOCKET_LIST             = 9004, // Node's inputs and outputs | Socket list
GFF_AC_SOCKET_IS_OUTPUT             = 9005, // Is this an output | Input or output?
GFF_AC_NODE_IMAGE                   = 9006, // Index in the image list | Image index
GFF_AC_EDGE_LIST                    = 9007, // Connectors in the graph | Connectors
GFF_AC_NODE_LIST                    = 9008, // Blend nodes | blend nodes
GFF_AC_NODE_COLOUR                  = 9009, // Blend node background colour | Background colour
GFF_AC_NODE_ANIMATION               = 9010, // Animation for stream node | Animation
GFF_AC_CURVE_CONTROL_POINT_LIST     = 9011, // List of control points for the curve | Curve control points
GFF_AC_CURVE_CONTROL_POINT_TIME     = 9012, // Time value for the control point | Control point time
GFF_AC_CURVE_CONTROL_POINT_VALUE    = 9013, // Value of the control point | Control point value
GFF_AC_MODEL_NAME                   = 9014, // Name of the model to be animated | Model name
GFF_AC_EVENT_LIST                   = 9015, // List of events | List of events
GFF_AC_EVENT_TIME                   = 9016, // Time at which the event fires | Event fire time
GFF_AC_EVENT_ID                     = 9017, // Event ID | Event ID
GFF_AC_NODE_LOOPING                 = 9018, // If true, this animation will be marked as looping | Looping animation
GFF_AC_FLAGS                        = 9019, // Various flags for a given file | Flags
GFF_AC_TRANS_ANIM_NAME              = 9020, // Transition animation name | Animation name
GFF_AC_TRANS_ANIM_START             = 9021, // Animation start time in transitions | Trans start time
GFF_AC_TRANS_ANIM_LENGTH            = 9022, // Animation length for transitions | Animation length
GFF_AC_TRANS_TRACK_LIST             = 9023, // List of animation structures for transitions (to/from) | Transition animations
GFF_AC_TRANSITION_LIST              = 9024, // List of transitions in the ACB file | Transitions
GFF_AC_TRANS_LENGTH                 = 9025, // Length of the transition | Transition length

GFF_AC_BLENDGROUP_ANIM_LIST         = 9100, // List of animation structures | Blend group animations
GFF_AC_BLEND_GROUP_LIST             = 9101, // List of blend groups | Blend groups
GFF_AC_BLENDGROUP_NAME              = 9102, // Name of the blend group | Group name

// animation composer range reserved up to 9999

// Binary GFF definitions (G2DA/.GDA files)
GFF_G2DA_COLUMN_NAME                = 10000, // Column Name | Human readable column name (debugging)
GFF_G2DA_COLUMN_HASH                = 10001, // Column Hash | 32-bit hash ID of column name string
GFF_G2DA_COLUMN_LIST                = 10002, // Column List | Table of column information
GFF_G2DA_ROW_LIST                   = 10003, // Row List | Table of row information
GFF_G2DA_ROW_DATA                   = 10004, // Row Data | Structure containing row variable data

GFF_G2DA_COLUMN_1                   = 10005, // Column Index
GFF_G2DA_COLUMN_2                   = 10006, // Column Index
GFF_G2DA_COLUMN_3                   = 10007, // Column Index
GFF_G2DA_COLUMN_4                   = 10008, // Column Index
GFF_G2DA_COLUMN_5                   = 10009, // Column Index
GFF_G2DA_COLUMN_6                   = 10010, // Column Index
GFF_G2DA_COLUMN_7                   = 10011, // Column Index
GFF_G2DA_COLUMN_8                   = 10012, // Column Index
GFF_G2DA_COLUMN_9                   = 10013, // Column Index
GFF_G2DA_COLUMN_10                  = 10014, // Column Index
GFF_G2DA_COLUMN_11                  = 10015, // Column Index
GFF_G2DA_COLUMN_12                  = 10016, // Column Index
GFF_G2DA_COLUMN_13                  = 10017, // Column Index
GFF_G2DA_COLUMN_14                  = 10018, // Column Index
GFF_G2DA_COLUMN_15                  = 10019, // Column Index
GFF_G2DA_COLUMN_16                  = 10020, // Column Index
GFF_G2DA_COLUMN_17                  = 10021, // Column Index
GFF_G2DA_COLUMN_18                  = 10022, // Column Index
GFF_G2DA_COLUMN_19                  = 10023, // Column Index
GFF_G2DA_COLUMN_20                  = 10024, // Column Index
GFF_G2DA_COLUMN_21                  = 10025, // Column Index
GFF_G2DA_COLUMN_22                  = 10026, // Column Index
GFF_G2DA_COLUMN_23                  = 10027, // Column Index
GFF_G2DA_COLUMN_24                  = 10028, // Column Index
GFF_G2DA_COLUMN_25                  = 10029, // Column Index
GFF_G2DA_COLUMN_26                  = 10030, // Column Index
GFF_G2DA_COLUMN_27                  = 10031, // Column Index
GFF_G2DA_COLUMN_28                  = 10032, // Column Index
GFF_G2DA_COLUMN_29                  = 10033, // Column Index
GFF_G2DA_COLUMN_30                  = 10034, // Column Index
GFF_G2DA_COLUMN_31                  = 10035, // Column Index
GFF_G2DA_COLUMN_32                  = 10036, // Column Index
GFF_G2DA_COLUMN_33                  = 10037, // Column Index
GFF_G2DA_COLUMN_34                  = 10038, // Column Index
GFF_G2DA_COLUMN_35                  = 10039, // Column Index
GFF_G2DA_COLUMN_36                  = 10040, // Column Index
GFF_G2DA_COLUMN_37                  = 10041, // Column Index
GFF_G2DA_COLUMN_38                  = 10042, // Column Index
GFF_G2DA_COLUMN_39                  = 10043, // Column Index
GFF_G2DA_COLUMN_40                  = 10044, // Column Index
GFF_G2DA_COLUMN_41                  = 10045, // Column Index
GFF_G2DA_COLUMN_42                  = 10046, // Column Index
GFF_G2DA_COLUMN_43                  = 10047, // Column Index
GFF_G2DA_COLUMN_44                  = 10048, // Column Index
GFF_G2DA_COLUMN_45                  = 10049, // Column Index
GFF_G2DA_COLUMN_46                  = 10050, // Column Index
GFF_G2DA_COLUMN_47                  = 10051, // Column Index
GFF_G2DA_COLUMN_48                  = 10052, // Column Index
GFF_G2DA_COLUMN_49                  = 10053, // Column Index
GFF_G2DA_COLUMN_50                  = 10054, // Column Index
GFF_G2DA_COLUMN_51                  = 10055, // Column Index
GFF_G2DA_COLUMN_52                  = 10056, // Column Index
GFF_G2DA_COLUMN_53                  = 10057, // Column Index
GFF_G2DA_COLUMN_54                  = 10058, // Column Index
GFF_G2DA_COLUMN_55                  = 10059, // Column Index
GFF_G2DA_COLUMN_56                  = 10060, // Column Index
GFF_G2DA_COLUMN_57                  = 10061, // Column Index
GFF_G2DA_COLUMN_58                  = 10062, // Column Index
GFF_G2DA_COLUMN_59                  = 10063, // Column Index
GFF_G2DA_COLUMN_60                  = 10064, // Column Index
GFF_G2DA_COLUMN_61                  = 10065, // Column Index
GFF_G2DA_COLUMN_62                  = 10066, // Column Index
GFF_G2DA_COLUMN_63                  = 10067, // Column Index
GFF_G2DA_COLUMN_64                  = 10068, // Column Index
GFF_G2DA_COLUMN_65                  = 10069, // Column Index
GFF_G2DA_COLUMN_66                  = 10070, // Column Index
GFF_G2DA_COLUMN_67                  = 10071, // Column Index
GFF_G2DA_COLUMN_68                  = 10072, // Column Index
GFF_G2DA_COLUMN_69                  = 10073, // Column Index
GFF_G2DA_COLUMN_70                  = 10074, // Column Index
GFF_G2DA_COLUMN_71                  = 10075, // Column Index
GFF_G2DA_COLUMN_72                  = 10076, // Column Index
GFF_G2DA_COLUMN_73                  = 10077, // Column Index
GFF_G2DA_COLUMN_74                  = 10078, // Column Index
GFF_G2DA_COLUMN_75                  = 10079, // Column Index
GFF_G2DA_COLUMN_76                  = 10080, // Column Index
GFF_G2DA_COLUMN_77                  = 10081, // Column Index
GFF_G2DA_COLUMN_78                  = 10082, // Column Index
GFF_G2DA_COLUMN_79                  = 10083, // Column Index
GFF_G2DA_COLUMN_80                  = 10084, // Column Index
GFF_G2DA_COLUMN_81                  = 10085, // Column Index
GFF_G2DA_COLUMN_82                  = 10086, // Column Index
GFF_G2DA_COLUMN_83                  = 10087, // Column Index
GFF_G2DA_COLUMN_84                  = 10088, // Column Index
GFF_G2DA_COLUMN_85                  = 10089, // Column Index
GFF_G2DA_COLUMN_86                  = 10090, // Column Index
GFF_G2DA_COLUMN_87                  = 10091, // Column Index
GFF_G2DA_COLUMN_88                  = 10092, // Column Index
GFF_G2DA_COLUMN_89                  = 10093, // Column Index
GFF_G2DA_COLUMN_90                  = 10094, // Column Index
GFF_G2DA_COLUMN_91                  = 10095, // Column Index
GFF_G2DA_COLUMN_92                  = 10096, // Column Index
GFF_G2DA_COLUMN_93                  = 10097, // Column Index
GFF_G2DA_COLUMN_94                  = 10098, // Column Index
GFF_G2DA_COLUMN_95                  = 10099, // Column Index
GFF_G2DA_COLUMN_96                  = 10100, // Column Index
GFF_G2DA_COLUMN_97                  = 10101, // Column Index
GFF_G2DA_COLUMN_98                  = 10102, // Column Index
GFF_G2DA_COLUMN_99                  = 10103, // Column Index

GFF_G2DA_COLUMN_100                 = 10104, // Column Index
GFF_G2DA_COLUMN_101                 = 10105, // Column Index
GFF_G2DA_COLUMN_102                 = 10106, // Column Index
GFF_G2DA_COLUMN_103                 = 10107, // Column Index
GFF_G2DA_COLUMN_104                 = 10108, // Column Index
GFF_G2DA_COLUMN_105                 = 10109, // Column Index
GFF_G2DA_COLUMN_106                 = 10110, // Column Index
GFF_G2DA_COLUMN_107                 = 10111, // Column Index
GFF_G2DA_COLUMN_108                 = 10112, // Column Index
GFF_G2DA_COLUMN_109                 = 10113, // Column Index
GFF_G2DA_COLUMN_110                 = 10114, // Column Index
GFF_G2DA_COLUMN_111                 = 10115, // Column Index
GFF_G2DA_COLUMN_112                 = 10116, // Column Index
GFF_G2DA_COLUMN_113                 = 10117, // Column Index
GFF_G2DA_COLUMN_114                 = 10118, // Column Index
GFF_G2DA_COLUMN_115                 = 10119, // Column Index
GFF_G2DA_COLUMN_116                 = 10120, // Column Index
GFF_G2DA_COLUMN_117                 = 10121, // Column Index
GFF_G2DA_COLUMN_118                 = 10122, // Column Index
GFF_G2DA_COLUMN_119                 = 10123, // Column Index
GFF_G2DA_COLUMN_120                 = 10124, // Column Index
GFF_G2DA_COLUMN_121                 = 10125, // Column Index
GFF_G2DA_COLUMN_122                 = 10126, // Column Index
GFF_G2DA_COLUMN_123                 = 10127, // Column Index
GFF_G2DA_COLUMN_124                 = 10128, // Column Index
GFF_G2DA_COLUMN_125                 = 10129, // Column Index
GFF_G2DA_COLUMN_126                 = 10130, // Column Index
GFF_G2DA_COLUMN_127                 = 10131, // Column Index
GFF_G2DA_COLUMN_128                 = 10132, // Column Index
GFF_G2DA_COLUMN_129                 = 10133, // Column Index
GFF_G2DA_COLUMN_130                 = 10134, // Column Index
GFF_G2DA_COLUMN_131                 = 10135, // Column Index
GFF_G2DA_COLUMN_132                 = 10136, // Column Index
GFF_G2DA_COLUMN_133                 = 10137, // Column Index
GFF_G2DA_COLUMN_134                 = 10138, // Column Index
GFF_G2DA_COLUMN_135                 = 10139, // Column Index
GFF_G2DA_COLUMN_136                 = 10140, // Column Index
GFF_G2DA_COLUMN_137                 = 10141, // Column Index
GFF_G2DA_COLUMN_138                 = 10142, // Column Index
GFF_G2DA_COLUMN_139                 = 10143, // Column Index
GFF_G2DA_COLUMN_140                 = 10144, // Column Index
GFF_G2DA_COLUMN_141                 = 10145, // Column Index
GFF_G2DA_COLUMN_142                 = 10146, // Column Index
GFF_G2DA_COLUMN_143                 = 10147, // Column Index
GFF_G2DA_COLUMN_144                 = 10148, // Column Index
GFF_G2DA_COLUMN_145                 = 10149, // Column Index
GFF_G2DA_COLUMN_146                 = 10150, // Column Index
GFF_G2DA_COLUMN_147                 = 10151, // Column Index
GFF_G2DA_COLUMN_148                 = 10152, // Column Index
GFF_G2DA_COLUMN_149                 = 10153, // Column Index
GFF_G2DA_COLUMN_150                 = 10154, // Column Index
GFF_G2DA_COLUMN_151                 = 10155, // Column Index
GFF_G2DA_COLUMN_152                 = 10156, // Column Index
GFF_G2DA_COLUMN_153                 = 10157, // Column Index
GFF_G2DA_COLUMN_154                 = 10158, // Column Index
GFF_G2DA_COLUMN_155                 = 10159, // Column Index
GFF_G2DA_COLUMN_156                 = 10160, // Column Index
GFF_G2DA_COLUMN_157                 = 10161, // Column Index
GFF_G2DA_COLUMN_158                 = 10162, // Column Index
GFF_G2DA_COLUMN_159                 = 10163, // Column Index
GFF_G2DA_COLUMN_160                 = 10164, // Column Index
GFF_G2DA_COLUMN_161                 = 10165, // Column Index
GFF_G2DA_COLUMN_162                 = 10166, // Column Index
GFF_G2DA_COLUMN_163                 = 10167, // Column Index
GFF_G2DA_COLUMN_164                 = 10168, // Column Index
GFF_G2DA_COLUMN_165                 = 10169, // Column Index
GFF_G2DA_COLUMN_166                 = 10170, // Column Index
GFF_G2DA_COLUMN_167                 = 10171, // Column Index
GFF_G2DA_COLUMN_168                 = 10172, // Column Index
GFF_G2DA_COLUMN_169                 = 10173, // Column Index
GFF_G2DA_COLUMN_170                 = 10174, // Column Index
GFF_G2DA_COLUMN_171                 = 10175, // Column Index
GFF_G2DA_COLUMN_172                 = 10176, // Column Index
GFF_G2DA_COLUMN_173                 = 10177, // Column Index
GFF_G2DA_COLUMN_174                 = 10178, // Column Index
GFF_G2DA_COLUMN_175                 = 10179, // Column Index
GFF_G2DA_COLUMN_176                 = 10180, // Column Index
GFF_G2DA_COLUMN_177                 = 10181, // Column Index
GFF_G2DA_COLUMN_178                 = 10182, // Column Index
GFF_G2DA_COLUMN_179                 = 10183, // Column Index
GFF_G2DA_COLUMN_180                 = 10184, // Column Index
GFF_G2DA_COLUMN_181                 = 10185, // Column Index
GFF_G2DA_COLUMN_182                 = 10186, // Column Index
GFF_G2DA_COLUMN_183                 = 10187, // Column Index
GFF_G2DA_COLUMN_184                 = 10188, // Column Index
GFF_G2DA_COLUMN_185                 = 10189, // Column Index
GFF_G2DA_COLUMN_186                 = 10190, // Column Index
GFF_G2DA_COLUMN_187                 = 10191, // Column Index
GFF_G2DA_COLUMN_188                 = 10192, // Column Index
GFF_G2DA_COLUMN_189                 = 10193, // Column Index
GFF_G2DA_COLUMN_190                 = 10194, // Column Index
GFF_G2DA_COLUMN_191                 = 10195, // Column Index
GFF_G2DA_COLUMN_192                 = 10196, // Column Index
GFF_G2DA_COLUMN_193                 = 10197, // Column Index
GFF_G2DA_COLUMN_194                 = 10198, // Column Index
GFF_G2DA_COLUMN_195                 = 10199, // Column Index
GFF_G2DA_COLUMN_196                 = 10200, // Column Index
GFF_G2DA_COLUMN_197                 = 10201, // Column Index
GFF_G2DA_COLUMN_198                 = 10202, // Column Index
GFF_G2DA_COLUMN_199                 = 10203, // Column Index

GFF_G2DA_COLUMN_200                 = 10204, // Column Index
GFF_G2DA_COLUMN_201                 = 10205, // Column Index
GFF_G2DA_COLUMN_202                 = 10206, // Column Index
GFF_G2DA_COLUMN_203                 = 10207, // Column Index
GFF_G2DA_COLUMN_204                 = 10208, // Column Index
GFF_G2DA_COLUMN_205                 = 10209, // Column Index
GFF_G2DA_COLUMN_206                 = 10210, // Column Index
GFF_G2DA_COLUMN_207                 = 10211, // Column Index
GFF_G2DA_COLUMN_208                 = 10212, // Column Index
GFF_G2DA_COLUMN_209                 = 10213, // Column Index
GFF_G2DA_COLUMN_210                 = 10214, // Column Index
GFF_G2DA_COLUMN_211                 = 10215, // Column Index
GFF_G2DA_COLUMN_212                 = 10216, // Column Index
GFF_G2DA_COLUMN_213                 = 10217, // Column Index
GFF_G2DA_COLUMN_214                 = 10218, // Column Index
GFF_G2DA_COLUMN_215                 = 10219, // Column Index
GFF_G2DA_COLUMN_216                 = 10220, // Column Index
GFF_G2DA_COLUMN_217                 = 10221, // Column Index
GFF_G2DA_COLUMN_218                 = 10222, // Column Index
GFF_G2DA_COLUMN_219                 = 10223, // Column Index
GFF_G2DA_COLUMN_220                 = 10224, // Column Index
GFF_G2DA_COLUMN_221                 = 10225, // Column Index
GFF_G2DA_COLUMN_222                 = 10226, // Column Index
GFF_G2DA_COLUMN_223                 = 10227, // Column Index
GFF_G2DA_COLUMN_224                 = 10228, // Column Index
GFF_G2DA_COLUMN_225                 = 10229, // Column Index
GFF_G2DA_COLUMN_226                 = 10230, // Column Index
GFF_G2DA_COLUMN_227                 = 10231, // Column Index
GFF_G2DA_COLUMN_228                 = 10232, // Column Index
GFF_G2DA_COLUMN_229                 = 10233, // Column Index
GFF_G2DA_COLUMN_230                 = 10234, // Column Index
GFF_G2DA_COLUMN_231                 = 10235, // Column Index
GFF_G2DA_COLUMN_232                 = 10236, // Column Index
GFF_G2DA_COLUMN_233                 = 10237, // Column Index
GFF_G2DA_COLUMN_234                 = 10238, // Column Index
GFF_G2DA_COLUMN_235                 = 10239, // Column Index
GFF_G2DA_COLUMN_236                 = 10240, // Column Index
GFF_G2DA_COLUMN_237                 = 10241, // Column Index
GFF_G2DA_COLUMN_238                 = 10242, // Column Index
GFF_G2DA_COLUMN_239                 = 10243, // Column Index
GFF_G2DA_COLUMN_240                 = 10244, // Column Index
GFF_G2DA_COLUMN_241                 = 10245, // Column Index
GFF_G2DA_COLUMN_242                 = 10246, // Column Index
GFF_G2DA_COLUMN_243                 = 10247, // Column Index
GFF_G2DA_COLUMN_244                 = 10248, // Column Index
GFF_G2DA_COLUMN_245                 = 10249, // Column Index
GFF_G2DA_COLUMN_246                 = 10250, // Column Index
GFF_G2DA_COLUMN_247                 = 10251, // Column Index
GFF_G2DA_COLUMN_248                 = 10252, // Column Index
GFF_G2DA_COLUMN_249                 = 10253, // Column Index
GFF_G2DA_COLUMN_250                 = 10254, // Column Index
GFF_G2DA_COLUMN_251                 = 10255, // Column Index
GFF_G2DA_COLUMN_252                 = 10256, // Column Index
GFF_G2DA_COLUMN_253                 = 10257, // Column Index
GFF_G2DA_COLUMN_254                 = 10258, // Column Index
GFF_G2DA_COLUMN_255                 = 10259, // Column Index
GFF_G2DA_COLUMN_256                 = 10260, // Column Index
GFF_G2DA_COLUMN_257                 = 10261, // Column Index
GFF_G2DA_COLUMN_258                 = 10262, // Column Index
GFF_G2DA_COLUMN_259                 = 10263, // Column Index
GFF_G2DA_COLUMN_260                 = 10264, // Column Index
GFF_G2DA_COLUMN_261                 = 10265, // Column Index
GFF_G2DA_COLUMN_262                 = 10266, // Column Index
GFF_G2DA_COLUMN_263                 = 10267, // Column Index
GFF_G2DA_COLUMN_264                 = 10268, // Column Index
GFF_G2DA_COLUMN_265                 = 10269, // Column Index
GFF_G2DA_COLUMN_266                 = 10270, // Column Index
GFF_G2DA_COLUMN_267                 = 10271, // Column Index
GFF_G2DA_COLUMN_268                 = 10272, // Column Index
GFF_G2DA_COLUMN_269                 = 10273, // Column Index
GFF_G2DA_COLUMN_270                 = 10274, // Column Index
GFF_G2DA_COLUMN_271                 = 10275, // Column Index
GFF_G2DA_COLUMN_272                 = 10276, // Column Index
GFF_G2DA_COLUMN_273                 = 10277, // Column Index
GFF_G2DA_COLUMN_274                 = 10278, // Column Index
GFF_G2DA_COLUMN_275                 = 10279, // Column Index
GFF_G2DA_COLUMN_276                 = 10280, // Column Index
GFF_G2DA_COLUMN_277                 = 10281, // Column Index
GFF_G2DA_COLUMN_278                 = 10282, // Column Index
GFF_G2DA_COLUMN_279                 = 10283, // Column Index
GFF_G2DA_COLUMN_280                 = 10284, // Column Index
GFF_G2DA_COLUMN_281                 = 10285, // Column Index
GFF_G2DA_COLUMN_282                 = 10286, // Column Index
GFF_G2DA_COLUMN_283                 = 10287, // Column Index
GFF_G2DA_COLUMN_284                 = 10288, // Column Index
GFF_G2DA_COLUMN_285                 = 10289, // Column Index
GFF_G2DA_COLUMN_286                 = 10290, // Column Index
GFF_G2DA_COLUMN_287                 = 10291, // Column Index
GFF_G2DA_COLUMN_288                 = 10292, // Column Index
GFF_G2DA_COLUMN_289                 = 10293, // Column Index
GFF_G2DA_COLUMN_290                 = 10294, // Column Index
GFF_G2DA_COLUMN_291                 = 10295, // Column Index
GFF_G2DA_COLUMN_292                 = 10296, // Column Index
GFF_G2DA_COLUMN_293                 = 10297, // Column Index
GFF_G2DA_COLUMN_294                 = 10298, // Column Index
GFF_G2DA_COLUMN_295                 = 10299, // Column Index
GFF_G2DA_COLUMN_296                 = 10300, // Column Index
GFF_G2DA_COLUMN_297                 = 10301, // Column Index
GFF_G2DA_COLUMN_298                 = 10302, // Column Index
GFF_G2DA_COLUMN_299                 = 10303, // Column Index

GFF_G2DA_COLUMN_TYPE                = 10999, // Column Type | enum of column data type
// G2DA reserved up to 10999

// Begin stage range

GFF_STAGE_PLACE_LIST                    = 11000, // Place List | List of places
GFF_STAGE_CAMERA_LIST                   = 11001, // Camera List | List of cameras
GFF_STAGE_PLACES_IN_SHOT                = 11002, // Places in Shot | List of places viewed by the camera
GFF_STAGE_CAMERA_FOV                    = 11003, // FOV | Camera field of view
GFF_STAGE_PLACE_DEFAULT_CAMERA          = 11004, // Default Camera | The default camera for the place
GFF_STAGE_CAMERA_DEPRECATED             = 11005, // Deprecated | Deprecated
GFF_STAGE_CAMERA_LOOKING_FROM           = 11006, // Look From | A place the camera is considered to be looking from
GFF_STAGE_CAMERA_LOOKING_AT_PRIMARY     = 11007, // Look At (Primary) | A Place the camera is Primary looking at
GFF_STAGE_CAMERA_LOOKING_AT_SECONDARY   = 11008, // Look At (Secondary) | A List of secondary places the camera looks at
GFF_STAGE_CAMERA_LOOKING_AT_TYPE        = 11009, // Look At Type | The type of lookat to be used

// Stage reserved up to 11999

// Begin conversation range

GFF_CONVERSATION_STARTING_LIST          = 12000, // Starting List | List of starts
GFF_CONVERSATION_STARTING_INDEX         = 12001, // Starting Index | Index of the starting node
GFF_CONVERSATION_LINE_LIST              = 12002, // Line List | List of conversation lines
GFF_CONVERSATION_END                    = 12003, // End Action | Actions executed when conversation ends
GFF_CONVERSATION_VOBANK                 = 12004, // VO Bank | VO Soundbank

GFF_CONVERSATION_STAGE_NAME             = 12100, // Stage Name | Name of the stage
GFF_CONVERSATION_STAGE_MAP              = 12101, // Stage Map | Mapping of object tags to place tags

GFF_CONVERSATION_KEY_TAG                = 12102, // Key Tag | Key tag of the map
GFF_CONVERSATION_VALUE_TAG              = 12103, // Value Tag | Value tag of the map

GFF_CONVERSATION_STAGE_AT_CURRENT_LOCATION = 12104, /// Stage At Current Location | Whether to place the stage origin at the location of the conversation owner

GFF_CONVERSATION_LINE_TEXT              = 12201, // Text | Text of the line
GFF_CONVERSATION_LINE_SPEAKER           = 12202, // Speaker | The speaker of the line
GFF_CONVERSATION_LINE_LISTENER          = 12203, // Listener | The listener of the line
GFF_CONVERSATION_LINE_GAME_LANGUAGE     = 12204, // Game Language | The in game language of the line
GFF_CONVERSATION_LINE_ICON              = 12205, // Icon | The line's icon
GFF_CONVERSATION_LINE_VISIBILITY        = 12206, // Visibility | The visibility of the line
GFF_CONVERSATION_LINE_AMBIENT           = 12207, // Ambient | Whether the line is ambient
GFF_CONVERSATION_LINE_COND              = 12208, // Condition | Conditional parameters of the line
GFF_CONVERSATION_LINE_ACTION            = 12209, // Action | Actions to take on the line
GFF_CONVERSATION_LINE_CUTSCENE_RESREF   = 12210, // Cutscene ResRef | ResRef of external cutscene
GFF_CONVERSATION_LINE_CUTSCENE          = 12211, // Cutscene | Embedded cutscene
GFF_CONVERSATION_LINE_CUTSCENE_MAP      = 12212, // Cutscene Map | Tag map for cutscene
GFF_CONVERSATION_LINE_ANIMATION         = 12213, // Speaker animation | Speaker animation
GFF_CONVERSATION_LINE_SKIP              = 12214, // Skip line | If true, don't play dialog on this line (cinematic conversations)
GFF_CONVERSATION_LINE_FASTPATH          = 12215, // Fast path | Quick choice for players who want to pick certain path (eg. fast/neutral)
GFF_CONVERSATION_LINE_NOVOINGAME        = 12216, // No VO in Game | If true, do not play related VO and FaceFX files
GFF_CONVERSATION_LINE_REVERT_ANIM       = 12217, // Revert anim | If true, revert speaker animation to idle at the end of the line
GFF_CONVERSATION_LINE_SLIDE_SHOW_TEXTURE= 12218, // Slide Show Texture | Texture to display in a slide-show format

GFF_CONVERSATION_PLOT_GUID              = 12300, // Plot GUID | The GUID of the plot to use
GFF_CONVERSATION_PLOT_FLAG              = 12301, // Plot Flag | The flag on the plot to use
GFF_CONVERSATION_PLOT_TEST              = 12302, // Plot Test | The test case to use on the plot
GFF_CONVERSATION_SCRIPT                 = 12303, // Script | The script to use
GFF_CONVERSATION_SCRIPT_PARAMETER       = 12304, // Script Parameter | The parameter to the script

GFF_CONVERSATION_LINE_CHILDREN_LIST     = 12400, // Children | List of children of this line

// TODO - these should be removed once the dependant code is checked in
GFF_CONVERSATION_STAGE_PLACE_TAG, 
GFF_CONVERSATION_STAGE_OBJECT_TAG, 

GFF_CONVERSATION_LINE_ACTIVE            = 12500, // Active | Objects that should get active/inactive during this line


// Conversation reserved up to 12999

// Begin plot range

GFF_PLOT_FLAGS                          = 13000, // Flags | List of plot flags
GFF_PLOT_FLAG_ID                        = 13001, // ID | ID to refer to the flag by
GFF_PLOT_FLAG_NAME                      = 13002, // Name | Name of the plot flag
GFF_PLOT_FLAG_REWARD                    = 13003, // Reward | ID of the plot reward
GFF_PLOT_FLAG_JOURNAL                   = 13004, // Journal | Journal text for the flag
GFF_PLOT_FLAG_ENDS_PLOT                 = 13005, // Ends Plot | Whether this flag ends the plot
GFF_PLOT_FLAG_MULTIREWARD               = 13006, // Multireward | Whetehr this reward can be given more than once
GFF_PLOT_GUID                           = 13007, // GUID | GUID of the plot
GFF_PLOT_NAME                           = 13008, // Name | Name of the plot
GFF_PLOT_SCRIPT                         = 13009, // Script | The script file associated with the plot
GFF_PLOT_PRIORITY                       = 13010, // Priority | The priority of the plot
GFF_PLOT_FLAGS1                         = 13011, // Flags1 | Default values of the plot flags
GFF_PLOT_FLAGS2                         = 13012, // Flags2 | Default values of the plot flags
GFF_PLOT_FLAGS3                         = 13013, // Flags3 | Default values of the plot flags
GFF_PLOT_FLAGS4                         = 13014, // Flags4 | Default values of the plot flags
GFF_PLOT_JOURNAL_IMAGE                  = 13015, // Journal Image | Image associated with journal entries for this plot
GFF_PLOT_PLOTS                          = 13016, // Plots | List of plots
GFF_PLOT_PARENT_PLOT                    = 13017, // Parent Plot | Plot that this is a sub-plot of
GFF_PLOT_FLAG_AREA_LOCATION_TAG         = 13018, // Area Location Tag | Location the plot flag is associated with
GFF_PLOTASSIST_LIST                     = 13019, // AssistInfo | list of plot assist info
GFF_PLOTASSIST_TAG                      = 13020, // PlotAdvancerTag | tag of something that becomes or stops being a plot destination
GFF_PLOTASSIST_ADVANCES_PLOT            = 13021, // AdvancesPlot | true if this guy now advances the plot
GFF_PLOT_ENTRYTYPE                      = 13022, // Entry Type | Type of plot entry (plot vs. codex)
GFF_PLOT_ALLOW_PAUSING                  = 13023, // Allow Pausing | true if plot allows pausing.
//JamesR Start
GFF_PLOT_FLAG_OFFERID                   = 13024, // OfferID | Offer this plot flag is associated with
//JamesR End
GFF_PLOT_PARENT_PLOT_GUID               = 13025, // Parent Plot GUID | Plot GUID that this is a sub-plot of

// Plot reserved up to 13999

// Begin tint range 

GFF_TINT_MASK_DIFFUSE_R                 = 14000, // Diff Red Channel | Diffuse Tint mask Red channel 
GFF_TINT_MASK_DIFFUSE_G                 = 14001, // Diff Green Channel | Diffuse Tint mask Green channel  
GFF_TINT_MASK_DIFFUSE_B                 = 14002, // Diff Blue Channel | Diffuse Tint mask Blue channel 
GFF_TINT_MASK_SPECULAR_R                = 14003, // Spec Red Channel | Specular Tint mask Red channel 
GFF_TINT_MASK_SPECULAR_G                = 14004, // Spec Green Channel | Specular Tint mask Green channel 
GFF_TINT_MASK_SPECULAR_B                = 14005, // Spec Blue Channel | Specular Tint mask Blue channel 
GFF_TINT_MASK_DIFFUSE_A                 = 14006, // Diffuse Alpha Channel | Diffuse tint mask alpha channel
GFF_TINT_MASK_SPECULAR_A                = 14007, // Specular Alpha Channel | Specular tint mask alpha channel
GFF_TINT_MASK_DIFFUSE_OPACITY           = 14008, // Diffuse tint opacity | Diffuse tint mask opacity values
GFF_TINT_MASK_SPECULAR_OPACITY          = 14009, // Specular tint opacity | Specular tint mask opacity values

// End tint range, reserved up to 14999

// Begin material range 

GFF_MAT_FILE_OBJECT_VERSION				= 15000, // Material project file version
GFF_MAT_CHILD_LIST						= 15001, // Child list | material editor child list

GFF_MAT_ROOT							= 15010, // Root | Root object in material editor
GFF_MAT_ROOT_NAME						= 15011, // Root name | Name of the root pbject
GFF_MAT_MODEL							= 15012, // Model | Model object in material editor
GFF_MAT_MODEL_NAME						= 15013, // Model name | Name of the model
GFF_MAT_PART							= 15014, // Model part | Part object in the model
GFF_MAT_PART_NAME						= 15015, // Part name | Name of the part object
GFF_MAT_PART_MMH_PARENT					= 15016, // Part MMH parent | Parent of the part in MMH hierarchy
GFF_MAT_MATLIB							= 15017, // MatLib | Material library object in material editor
GFF_MAT_MATLIB_NAME						= 15018, // MatLib name | Name of the material library
GFF_MAT_MATOBJ							= 15019, // MatObj | Material object in the material editor
GFF_MAT_MATOBJ_NAME						= 15020, // MatObj name | Name of the material object
GFF_MAT_LIGHT							= 15021, // Light | Light object in material editor
GFF_MAT_LIGHT_NAME						= 15022, // Light name | Name of the light object
GFF_MAT_LIGHT_RIG						= 15023, // Light rig | Light rig object in material editor
GFF_MAT_LIGHT_RIG_NAME					= 15024, // Light rig name | Name of the light rig object
GFF_MAT_LIGHT_PROBE						= 15025, // Light probe | Light probe object in material editor
GFF_MAT_LIGHT_PROBE_NAME				= 15026, // Light probe name | Name of light probe
GFF_MAT_GROUP                           = 15027, // Group | Group object in material editor
GFF_MAT_GROUP_NAME                      = 15028, // Group name | Name of the group object
GFF_MAT_PALETTELIB						= 15029, // PaletteLib | Palette library object in material editor
GFF_MAT_PALETTELIB_NAME					= 15030, // PaletteLib name | Name of the palette library
GFF_MAT_PALETTEOBJ						= 15031, // PaletteObj | Palette object in the material editor
GFF_MAT_PALETTEOBJ_NAME					= 15032, // PaletteObj name | Name of the palette object
GFF_MAT_HERALDRYLIB						= 15033, // HeraldryLib | Heraldry library object in material editor
GFF_MAT_HERALDRYLIB_NAME				= 15034, // HeraldryLib name | Name of the Heraldry library
GFF_MAT_HERALDRYOBJ						= 15035, // HeraldryObj | Heraldry object in the material editor
GFF_MAT_HERALDRYOBJ_NAME				= 15036, // HeraldryObj name | Name of the Heraldry object
GFF_MAT_DUPLICATE						= 15037, // Duplicate | Duplicate object in material editor
GFF_MAT_DUPLICATE_NAME					= 15038, // Duplicate name | Name of the Duplicate
GFF_MAT_LAYOUT_NAME						= 15039, // Layout name | Name of the layout
GFF_MAT_TINTLIB							= 15040, // TintLib | Tint library object in material editor
GFF_MAT_TINTLIB_NAME					= 15041, // TintLib name | Name of the tint library
GFF_MAT_TINTOBJ							= 15042, // TintObj | Tint object in the material editor
GFF_MAT_TINTOBJ_NAME					= 15043, // TintObj name | Name of the tint object

// basic params
GFF_MAT_MATERIAL_TYPE					= 15050, // Material type | Material type, static or character
GFF_MAT_BASIC_PARAMS					= 15051, // Basic parameters | Basic material parameters
GFF_MAT_SHINY_TRANS						= 15052, // Shiny Transparent | Shiny transparent
GFF_MAT_TWO_SIDE						= 15053, // Two side | Two sided material
GFF_MAT_HAIR							= 15054, // Hair | Hair material
GFF_MAT_DYNC_LIGHT						= 15055, // Dynamic light | Dynamic light mode
GFF_MAT_BLEND_MODE						= 15056, // Blend mode | Blend mode for the material
GFF_MAT_NAME							= 15057, // Mat name | Name of the material object used by the MMH file
GFF_MAT_MATERIAL_TYPE_STRING			= 15058, // Material type | Material type, string
GFF_MAT_MATERIAL_SEMANTIC				= 15059, // Material Semantic | Material Semantic
GFF_MAT_MATERIAL_SOUND_TYPE             = 15060, // Material sound type | Material sound type

// diffuse
GFF_MAT_DIFFUSE_MAP_TYPE				= 15070, // Diffuse map type | Type of the diffuse map
GFF_MAT_DIFFUSE_MAP_COLOR				= 15071, // Diffuse map color | Color of the diffuse map
GFF_MAT_DIFFUSE_MAP_SCALE				= 15072, // Diffuse map scale | Scale of the diffuse map
GFF_MAT_DIFFUSE_MAP						= 15073, // Diffuse map | Texture of the diffuse map
GFF_MAT_DIFFUSE_FILENAME				= 15074, // Diffuse file name | Diffuse map name used in MAL file
GFF_MAT_DIFFOPAC_DIMENSIONX				= 15075, // Diffuse/opacity dimension X | Dimension X of the diffuse map used in MAL file
GFF_MAT_DIFFOPAC_DIMENSIONY				= 15076, // Diffuse/opacity dimension Y | Dimension Y of the diffuse map used in MAL file
GFF_MAT_DIFFOPAC_COMPRESSION			= 15077, // Diffuse/opacity compression | Compression type
GFF_MAT_DIFFOPAC_COMPRESSION_XBOX360    = 15078, // Diffuse/opacity compression for xbox 360 | Compression type

// secondary diffuse
GFF_MAT_SECONDARY_DIFFUSE_MAP_ENABLE             = 15080, // Secondary Diffuse map | Texture of the secondary diffuse map
GFF_MAT_SECONDARY_DIFFUSE_MAP					= 15081, // Secondary Diffuse map | Texture of the secondary diffuse map
GFF_MAT_SECONDARY_DIFFUSE_FILENAME				= 15082, // Secondary Diffuse file name | Secondary Diffuse map name used in MAL file
GFF_MAT_SECONDARY_DIFFUSE_COMPRESSION			= 15085, // Secondary Diffuse/opacity compression | Compression type
GFF_MAT_SECONDARY_DIFFUSE_COMPRESSION_XBOX360    = 15086, // Secondary Diffuse/opacity compression for xbox 360 | Compression type

// opacity
GFF_MAT_OPACITYMAPENABLE				= 15100, // Opacity map enable | Enable/disable using opacity map
GFF_MAT_OPACITYMAPTYPE					= 15101, // Opacity map type | Type of the opacity map
GFF_MAT_OPACITYMAPCOLOR					= 15102, // Opacity map color | Color of the opacity map
GFF_MAT_OPACITYMAPSCALE					= 15103, // Opacity map scale | Scale of the opacity map
GFF_MAT_OPACITYMAP						= 15104, // Opacity map | Texture file of the opacity map

// specular
GFF_MAT_SPECULAR_MAP_ENABLE				= 15130, // Specular map enable | Enable/disable of the specular map
GFF_MAT_SPECULAR_MAP_TYPE				= 15131, // Specular map type | Type of the specular map
GFF_MAT_SPECULAR_MAP_COLOR				= 15132, // Specular map color | Color of the specular map
GFF_MAT_SPECULAR_MAP_SCALE				= 15133, // Specular map scale | Scale of the specular map
GFF_MAT_SPECULAR_MAP					= 15134, // Specualr map | Texture file of the specualr map
GFF_MAT_SPECULAR_GLOSS_TYPE				= 15135, // Specular glossiness type | Type of the specular glossiness
GFF_MAT_SPECULAR_GLOSS_COLOR			= 15136, // Specular glossiness color | Color of the specular glossiness
GFF_MAT_SPECULAR_GLOSS_SCALE			= 15137, // Specular glossiness scale | Scale of the specular glossiness
GFF_MAT_SPECULAR_GLOSS					= 15138, // Specular glossiness map | Texture file of the specular glossiness map
GFF_MAT_SPECULAR_FILENAME				= 15139, // Specular file name | Texture file used in MAL file
GFF_MAT_SPECULAR_DIMENSIONX				= 15140, // Specular dimension X | Dimension X of the specular map
GFF_MAT_SPECULAR_DIMENSIONY				= 15141, // Specular dimension Y | Dimension Y of the specular map
GFF_MAT_SPECULAR_COMPRESSION			= 15142, // Specular compression | Compression type of the specular map
GFF_MAT_SPECULAR_COMPRESSION_XBOX360    = 15143, // Specular compression for xbox 360 | Compression type of the specular map
GFF_MAT_SPECULAR_REFLECTION_MULTIPLIER  = 15144, // Specular multiplier | Specular multiplier for environment reflection

// normal
GFF_MAT_NORMAL_MAP_ENABLE				= 15160, // Normal map enable | Enable/disable normal map
GFF_MAT_NORMAL_MAP						= 15161, // Normal map | Texture of the normal map
GFF_MAT_NORMAL_FILENAME					= 15162, // Normal map file name | Texture file used in MAL file
GFF_MAT_NORMAL_COMPRESSION              = 15163, // Normal map compression | Compression Type
GFF_MAT_NORMAL_COMPRESSION_XBOX360      = 15164, // Normal map compression for xbox 360 | Compression Type

// tint mask
GFF_MAT_TINT_MAP_ENABLE					= 15190, // Tint map enable | Enable/disable tint map
GFF_MAT_TINT_MAP						= 15191, // Tint map | Texture of the tine map

// tint object properties
GFF_MAT_TINT_R_ENABLE					= 15192, // Tint R enable | Enable/disable R channel
GFF_MAT_TINT_G_ENABLE					= 15193, // Tint G enable | Enable/disable G channel
GFF_MAT_TINT_B_ENABLE					= 15194, // Tint B enable | Enable/disable B channel
GFF_MAT_TINT_FILENAME_POSTFIX           = 15195, // TNT file name | Name of the TNT file

// tint mask cont...
GFF_MAT_TINT_COMPRESSION                = 15196, // Tint map compression | Compression type
GFF_MAT_TINT_COMPRESSION_XBOX360        = 15197, // Tint map compression for xbox 360 | Compression type

// tint object properties cont..
GFF_MAT_TINT_A_ENABLE					= 15198, // Tint A enable | Enable/disable A channel
GFF_MAT_TINT_R_SPECULAR_INTENSITY		= 15199, // Tint R specular intensity | Tint R specular intensity
GFF_MAT_TINT_G_SPECULAR_INTENSITY		= 15200, // Tint G specular intensity | Tint G specular intensity
GFF_MAT_TINT_B_SPECULAR_INTENSITY		= 15201, // Tint B specular intensity | Tint B specular intensity
GFF_MAT_TINT_A_SPECULAR_INTENSITY		= 15202, // Tint A specular intensity | Tint A specular intensity
GFF_MAT_TINT_R_DIFFUSE_INTENSITY		= 15203, // Tint R diffuse intensity | Tint R diffuse intensity
GFF_MAT_TINT_G_DIFFUSE_INTENSITY		= 15204, // Tint G diffuse intensity | Tint G diffuse intensity
GFF_MAT_TINT_B_DIFFUSE_INTENSITY		= 15205, // Tint B diffuse intensity | Tint B diffuse intensity
GFF_MAT_TINT_A_DIFFUSE_INTENSITY		= 15206, // Tint A diffuse intensity | Tint A diffuse intensity
GFF_MAT_TINT_R_SPECULAR_OPACITY			= 15207, // Tint R specular OPACITY | Tint R specular OPACITY
GFF_MAT_TINT_G_SPECULAR_OPACITY			= 15208, // Tint G specular OPACITY | Tint G specular OPACITY
GFF_MAT_TINT_B_SPECULAR_OPACITY			= 15209, // Tint B specular OPACITY | Tint B specular OPACITY
GFF_MAT_TINT_A_SPECULAR_OPACITY			= 15210, // Tint A specular OPACITY | Tint A specular OPACITY
GFF_MAT_TINT_R_DIFFUSE_OPACITY			= 15211, // Tint R diffuse OPACITY | Tint R diffuse OPACITY
GFF_MAT_TINT_G_DIFFUSE_OPACITY			= 15212, // Tint G diffuse OPACITY | Tint G diffuse OPACITY
GFF_MAT_TINT_B_DIFFUSE_OPACITY			= 15213, // Tint B diffuse OPACITY | Tint B diffuse OPACITY
GFF_MAT_TINT_A_DIFFUSE_OPACITY			= 15214, // Tint A diffuse OPACITY | Tint A diffuse OPACITY
GFF_MAT_TINT_TYPE			            = 15215, // Tint Type | Tint Type

// tint mask map cont... again...
GFF_MAT_TINT_MASK_TINT_CHANNEL1         = 15216, // Tint File Name | Tint Mask Selected Tint File for Channel 1
GFF_MAT_TINT_MASK_TINT_CHANNEL2         = 15217, // Tint File Name | Tint Mask Selected Tint File for Channel 2
GFF_MAT_TINT_MASK_TINT_CHANNEL3         = 15218, // Tint File Name | Tint Mask Selected Tint File for Channel 3
GFF_MAT_TINT_MASK_TINT_CHANNEL4         = 15219, // Tint File Name | Tint Mask Selected Tint File for Channel 4

// relief
GFF_MAT_RELIEF_MAP_ENABLE				= 15220, // Relief map enable | Enable/disable relief map
GFF_MAT_RELIEF_MAP						= 15221, // Relief map | Texture of the tint map
GFF_MAT_RELIEF_MAP_SCALE                = 15222, // Relief map scale | Scale of relief map
GFF_MAT_RELIEF_MAP_SAMPLES              = 15223, // Relief map samples | Samples on relief map
GFF_MAT_RELIEF_MAP_SHADOW_OFFSET        = 15224, // Relief map offset | Offset for relief map
GFF_MAT_RELIEF_MAP_IN_OUT               = 15225, // Relief map in/out | In/out for relief map
GFF_MAT_RELIEF_COMPRESSION              = 15226, // Relief map compression | Compression type
GFF_MAT_RELIEF_COMPRESSION_XBOX360      = 15227, // Relief map compression for xbox 360 | Compression type

// more tint object properties...
GFF_MAT_TINT_EXPORTABLE                 = 15228, // Tint object exportable | Tint object exportable

// vfx
GFF_MAT_VFX_CONTACT_SHEET_WIDTH			= 15250, // VFX contact sheet width | Contact sheet width
GFF_MAT_VFX_CONTACT_SHEET_HEIGHT		= 15251, // VFX contact sheet height | Contact sheet height
GFF_MAT_VFX_CONTACT_SHEET_FRAMES		= 15252, // VFX contact sheet frames | Contact sheet frames
GFF_MAT_VFX_SCROLL_SPEED_U				= 15253, // VFX U scroll speed | U scroll speed
GFF_MAT_VFX_SCROLL_SPEED_V				= 15254, // VFX V scroll speed | V scroll speed
GFF_MAT_VFX_DEPTH_BIAS_ALPHA     		= 15255, // VFX Depth bias alpha value | Depth bias alpha value
GFF_MAT_VFX_START_ALPHA_FRESNEL         = 15256, // VFX fresnel start | Alpha fresnel falloff start angle
GFF_MAT_VFX_END_ALPHA_FRESNEL           = 15257, // VFX fresnel end | Alpha fresnel falloff end angle
GFF_MAT_VFX_INVERT_ALPHA_FRESNEL        = 15258, // VFX fresnel invert | Alpha fresnel falloff invert

// fresnel
GFF_MAT_FRESNEL_MAP_ENABLE				= 15280, // Fresnel map enable | Enable/disable of the Fresnel map
GFF_MAT_FRESNEL_MAP						= 15281, // Fresnel map | Texture file of the Fresnel map
GFF_MAT_FRESNEL_FILENAME				= 15282, // Fresnel file name | Texture file used in MAL file
GFF_MAT_FRESNEL_COMPRESSION				= 15283, // Fresnel compression | Compression type of the Fresnel map
GFF_MAT_FRESNEL_COMPRESSION_XBOX360		= 15284, // Fresnel compression for xbox 360 | Compression type of the Fresnel map

// emissive
GFF_MAT_EMISSIVE_MAP_ENABLE				= 15310, // Emissive map enable | Enable/disable of the Emissive map
GFF_MAT_EMISSIVE_MAP					= 15311, // Emissive map | Texture file of the Emissive map
GFF_MAT_EMISSIVE_FILENAME				= 15312, // Emissive file name | Texture file used in MAL file
GFF_MAT_EMISSIVE_COMPRESSION			= 15313, // Emissive compression | Compression type of the Emissive map
GFF_MAT_EMISSIVE_COMPRESSION_XBOX360	= 15314, // Emissive compression for xbox 360 | Compression type of the Emissive map

// section mask
GFF_MAT_SECTION_MASK_MAP_ENABLE				= 15340, // UNUSED
GFF_MAT_SECTION_MASK_MAP					= 15341, // UNUSED
GFF_MAT_SECTION_MASK_FILENAME			    = 15342, // UNUSED
GFF_MAT_SECTION_MASK_COMPRESSION			= 15343, // UNUSED
GFF_MAT_SECTION_MASK_COMPRESSION_XBOX360	= 15344, // UNUSED

// secondary normal
GFF_MAT_SECONDARY_NORMAL_MAP_ENABLE			= 15360, // Secondary Normal map enable | Enable/disable Secondary normal map
GFF_MAT_SECONDARY_NORMAL_MAP				= 15361, // Secondary Normal map | Texture of the Secondary normal map
GFF_MAT_SECONDARY_NORMAL_FILENAME			= 15362, // Secondary Normal map file name | Texture file used in MAL file
GFF_MAT_SECONDARY_NORMAL_COMPRESSION        = 15363, // Secondary Normal map compression | Compression Type
GFF_MAT_SECONDARY_NORMAL_COMPRESSION_XBOX360= 15364, // Secondary Normal map compression for xbox 360 | Compression Type

// eye params
GFF_MAT_EYE_CORNEA_SPECULAR_MASK			    = 15380, // Cornea specular mask | Cornea specular mask
GFF_MAT_EYE_CORNEA_SPECULAR_POWER		        = 15381, // Cornea specular power | Cornea specular power
GFF_MAT_EYE_SCLERA_SPECULAR_MASK    	        = 15382, // Sclera specular mask | Sclera specular mask
GFF_MAT_EYE_SCLERA_SPECULAR_POWER               = 15383, // Sclera specular power | Sclera specular mask
GFF_MAT_EYE_CORNEA_REFLECTION_MULTIPLIER	    = 15384, // UNUSED

// Packed Texture
GFF_MAT_SPECULAR_MASK_MAP_ENABLE			 = 15400, // UNUSED
GFF_MAT_PACKED_TEXTURE_MAP				     = 15401, // Packed Texture map | Texture of the Packed Texture map
GFF_MAT_PACKED_TEXTURE_FILENAME			     = 15402, // Packed Texture map file name | Texture file used in MAL file
GFF_MAT_PACKED_TEXTURE_COMPRESSION           = 15403, // Packed Texture map compression | Compression Type
GFF_MAT_PACKED_TEXTURE_COMPRESSION_XBOX360   = 15404, // Packed Texture map compression for xbox 360 | Compression Type

// Tint Noise
GFF_MAT_SPECULAR_SHIFT_MAP_ENABLE			= 15420, // UNUSED
GFF_MAT_TINT_NOISE_MAP				        = 15421, // Tint Noise map | Texture of the Tint Noise map
GFF_MAT_TINT_NOISE_FILENAME			        = 15422, // Tint Noise map file name | Texture file used in MAL file
GFF_MAT_TINT_NOISE_COMPRESSION              = 15423, // Tint Noise map compression | Compression Type
GFF_MAT_TINT_NOISE_COMPRESSION_XBOX360      = 15424, // Tint Noise map compression for xbox 360 | Compression Type

// hair params
GFF_MAT_HAIR_DIFFUSE_TINT			        = 15440, // Diffuse Tint | Diffuse Tint color
GFF_MAT_HAIR_PRIMARY_SPECULAR_POWER		    = 15441, // Primary Specular Power | Primary Specular Power
GFF_MAT_HAIR_PRIMARY_SPECULAR_MASK	        = 15442, // Primary Specular Multiplier | Primary Specular Multiplier
GFF_MAT_HAIR_SECONDARY_SPECULAR_POWER       = 15443, // Secondary Specular Power | Secondary Specular Power
GFF_MAT_HAIR_SECONDARY_SPECULAR_TINT        = 15444, // Secondary Specular Tint | Secondary Specular Tint
GFF_MAT_HAIR_TINT_NOISE_TILING   		    = 15445, // Tint Noise Tiling | Tint Noise Tiling

// Sun light
GFF_MAT_SUN									= 15460, // Sun | Sun object in the material editor
GFF_MAT_SUN_NAME							= 15461, // Sun name | Name of the sun
GFF_MAT_SUN_DIRECTION						= 15462, // SunlightDirection | vector, the direction of the sunlight
GFF_MAT_SUN_COLOR							= 15463, // SunlightColor | Color, the color of the sunlight
GFF_MAT_SUN_COLORMULT						= 15464, // SunlightColorMultiplier | float32, multiplier for the sunlight color

// heraldry
GFF_MAT_HERALDRY_MAP_ENABLE					= 15480, // Heraldry map enable | Enable/disable Heraldry map
GFF_MAT_HERALDRY_MAP						= 15481, // Heraldry map | Texture of the Heraldry map
GFF_MAT_HERALDRY_FILENAME					= 15482, // Heraldry map file name | Texture file used in MAL file
GFF_MAT_HERALDRY_COMPRESSION				= 15483, // Heraldry map compression | Compression Type
GFF_MAT_HERALDRY_COMPRESSION_XBOX360		= 15484, // Heraldry map compression for xbox 360 | Compression Type

// character params
GFF_MAT_RIM_LIGHT_WIDTH						= 15500, // Rim Light Width | Rim Light Width
GFF_MAT_RIM_LIGHT_MULTIPLIER				= 15501, // Rim Light Multiplier | Rim Light Multiplier
GFF_MAT_FALLOFF_WIDTH                       = 15502, // Falloff Width | Falloff Width
GFF_MAT_FALLOFF_MULTIPLIER                  = 15503, // Falloff Multiplier | Falloff Multiplier

// Face params
GFF_MAT_AMBIENT_MULTIPLIER					= 15510, // Ambient Multiplier | Ambient Multiplier
GFF_MAT_SPECULAR_MULTIPLIER                 = 15511, // Specular Multiplier | Specular Multiplier
GFF_MAT_LIP_SPECULAR_BOOST                  = 15512, // Lip Specular Boost | Specular Boost for the lips
GFF_MAT_RIM_POWER                           = 15513, // Rim Power | Rim Power

// distortion
GFF_MAT_DISTORTION_MAP_ENABLE				= 15520, // Distortion map enable | Enable/disable of the Distortion map
GFF_MAT_DISTORTION_MAP						= 15521, // Distortion map | Texture file of the Distortion map
GFF_MAT_DISTORTION_FILENAME					= 15522, // Distortion file name | Texture file used in MAL file
GFF_MAT_DISTORTION_COMPRESSION				= 15523, // Distortion compression | Compression type of the Distortion map
GFF_MAT_DISTORTION_COMPRESSION_XBOX360		= 15524, // Distortion compression for xbox 360 | Compression type of the Distortion map

// distortion modifiers
GFF_MAT_DISTORTIONMODIFIERS_MAP_ENABLE			= 15540, // DistortionModifiers map enable | Enable/disable of the DistortionModifiers map
GFF_MAT_DISTORTIONMODIFIERS_MAP					= 15541, // DistortionModifiers map | Texture file of the DistortionModifiers map
GFF_MAT_DISTORTIONMODIFIERS_FILENAME			= 15542, // DistortionModifiers file name | Texture file used in MAL file
GFF_MAT_DISTORTIONMODIFIERS_COMPRESSION			= 15543, // DistortionModifiers compression | Compression type of the DistortionModifiers map
GFF_MAT_DISTORTIONMODIFIERS_COMPRESSION_XBOX360	= 15544, // DistortionModifiers compression for xbox 360 | Compression type of the DistortionModifiers map

// distortion params
GFF_MAT_DISTORTION_MAGNITUDE					= 15560, // Distortion magnitude | Distortion magnitude
GFF_MAT_DISTORTION_INVERT						= 15561, // Distortion invert | Distortion invert
GFF_MAT_DISTORTION_FADE_DISTANCE				= 15562, // Distortion fade distance | Distortion fade distance
GFF_MAT_DISTORTION_FADE_MULTIPLIER				= 15563, // Distortion fade multiplier | Distortion fade multiplier

// alternate decal map
GFF_MAT_ALTERNATE_DECAL_MAP						= 15580, // Alternate decal map | Texture of the diffuse map
GFF_MAT_ALTERNATE_DECAL_FILENAME				= 15581, // Alternate decal file name | Diffuse map name used in MAL file
GFF_MAT_ALTERNATE_DECAL_COMPRESSION			    = 15582, // Alternate decal compression | Compression type
GFF_MAT_ALTERNATE_DECAL_COMPRESSION_XBOX360     = 15583, // Alternate decal compression for xbox 360 | Compression type

// Tattoo Mask
GFF_MAT_TATTOO_MASK_MAP				            = 15590, // Tattoo Mask map | Texture of the Tattoo Mask map
GFF_MAT_TATTOO_MASK_FILENAME			        = 15591, // Tattoo Mask map file name | Texture file used in MAL file
GFF_MAT_TATTOO_MASK_COMPRESSION                 = 15592, // Tattoo Mask map compression | Compression Type
GFF_MAT_TATTOO_MASK_COMPRESSION_XBOX360         = 15593, // Tattoo Mask map compression for xbox 360 | Compression Type
GFF_MAT_TATTOO_MASK_MAP_ENABLE				    = 15594, // Tattoo Mask map enable | Enable/disable of the Tattoo Mask map

GFF_MAT_TATTOO_MASK_TINT_CHANNEL1               = 15595, // Tint File Name | Tattoo Mask Selected Tint File for Channel 1
GFF_MAT_TATTOO_MASK_TINT_CHANNEL2               = 15596, // Tint File Name | Tattoo Mask Selected Tint File for Channel 2
GFF_MAT_TATTOO_MASK_TINT_CHANNEL3               = 15597, // Tint File Name | Tattoo Mask Selected Tint File for Channel 3
GFF_MAT_TATTOO_MASK_TINT_CHANNEL4               = 15598, // Tint File Name | Tattoo Mask Selected Tint File for Channel 4

// Brow Stubble
GFF_MAT_BROW_STUBBLE_MAP				        = 15600, // Brow Stubble map | Texture of the Brow Stubble map
GFF_MAT_BROW_STUBBLE_FILENAME			        = 15601, // Brow Stubble map file name | Texture file used in MAL file
GFF_MAT_BROW_STUBBLE_COMPRESSION                = 15602, // Brow Stubble map compression | Compression Type
GFF_MAT_BROW_STUBBLE_COMPRESSION_XBOX360        = 15603, // Brow Stubble map compression for xbox 360 | Compression Type

// Brow Stubble Normal
GFF_MAT_BROW_STUBBLE_NORMAL_MAP				    = 15610, // Brow Stubble Normal map | Texture of the Brow Stubble Normal map
GFF_MAT_BROW_STUBBLE_NORMAL_FILENAME			= 15611, // Brow Stubble Normal map file name | Texture file used in MAL file
GFF_MAT_BROW_STUBBLE_NORMAL_COMPRESSION         = 15612, // Brow Stubble Normal map compression | Compression Type
GFF_MAT_BROW_STUBBLE_NORMAL_COMPRESSION_XBOX360 = 15613, // Brow Stubble Normal map compression for xbox 360 | Compression Type

// Emotions Mask 0
GFF_MAT_EMOTIONS_MASK_0_MAP				        = 15620, // Emotions Mask 0 map | Texture of the Emotions Mask 0 map
GFF_MAT_EMOTIONS_MASK_0_FILENAME			    = 15621, // Emotions Mask 0 map file name | Texture file used in MAL file
GFF_MAT_EMOTIONS_MASK_0_COMPRESSION             = 15622, // Emotions Mask 0 map compression | Compression Type
GFF_MAT_EMOTIONS_MASK_0_COMPRESSION_XBOX360     = 15623, // Emotions Mask 0 map compression for xbox 360 | Compression Type

// Emotions Mask 1
GFF_MAT_EMOTIONS_MASK_1_MAP				        = 15630, // Emotions Mask 1 map | Texture of the Emotions Mask 1 map
GFF_MAT_EMOTIONS_MASK_1_FILENAME			    = 15631, // Emotions Mask 1 map file name | Texture file used in MAL file
GFF_MAT_EMOTIONS_MASK_1_COMPRESSION             = 15632, // Emotions Mask 1 map compression | Compression Type
GFF_MAT_EMOTIONS_MASK_1_COMPRESSION_XBOX360     = 15633, // Emotions Mask 1 map compression for xbox 360 | Compression Type

// Emotions Normal
GFF_MAT_EMOTIONS_NORMAL_MAP				        = 15640, // Emotions Normal map | Texture of the Emotions Normal map
GFF_MAT_EMOTIONS_NORMAL_FILENAME			    = 15641, // Emotions Normal map file name | Texture file used in MAL file
GFF_MAT_EMOTIONS_NORMAL_COMPRESSION             = 15642, // Emotions Normal map compression | Compression Type
GFF_MAT_EMOTIONS_NORMAL_COMPRESSION_XBOX360     = 15643, // Emotions Normal map compression for xbox 360 | Compression Type

// Lava
GFF_MAT_SCROLL_SPEED_1                          = 15650, // Texture scroll speed | Texture scroll speed
GFF_MAT_SCROLL_SPEED_2                          = 15651, // Texture scroll speed | Texture scroll speed
GFF_MAT_SCROLL_SPEED_3                          = 15652, // Texture scroll speed | Texture scroll speed
GFF_MAT_LAVA_TINT_COLOR                         = 15653, // Lava tint color | Lava tint color
GFF_MAT_LAVA_BRIGHTNESS                         = 15654, // Lava brightness | Lava brightness
GFF_MAT_LAVA_CONTRAST                           = 15655, // Lava contrast | Lava contrast
GFF_MAT_LAVA_NOISE_MAP                          = 15656, // Lava noise texture | Lava material noise texture

// End material range, reserved up to 15999

// Begin Save Game Range

// Top-level
GFF_SAVEGAME_CAMPAIGN           = 16000, // Campaign | Save game Campaign info
GFF_SAVEGAME_AREALIST           = 16001, // Areas | Area list in save game.
GFF_SAVEGAME_PLAYERCHAR         = 16002, // Player Character | The player's character in the save game.
GFF_SAVEGAME_PARTYLIST          = 16003, // Party List | The list of party members.
GFF_SAVEGAME_VERSION            = 16004, // Save game version information | The savegame version information. (The private build number for this save on old saves).
GFF_SAVEGAME_GAME_STATE         = 16005, // Game State | The state of the game of the current save.
GFF_SAVEGAME_ADDINSLIST         = 16006, // Active Add-Ins | List of all Add-Ins active at save time.
GFF_SAVEGAME_CHEAT_USED         = 16007, // Save game cheat information | Specifies if a cheat has been used in this save game.
GFF_SAVEGAME_STORYSOFAR			= 16008, // Story So Far | The events tracked in the hero's story (so far).

// Area properties and object lists
GFF_SAVEGAME_AREA_PLACEABLES    = 16010, // Placeables | Placeables
GFF_SAVEGAME_AREA_CREATURES     = 16011, // Creatures | Creatures
GFF_SAVEGAME_AREA_TRIGGERS      = 16012, // Triggers | Triggers
GFF_SAVEGAME_AREA_AOES          = 16013, // Area of Effect Objects | Area of Effect Objects
GFF_SAVEGAME_CAMPAIGN_RESOURCE  = 16014, // Campaign Resource | The name of the directory the module is in.
GFF_SAVEGAME_AREA_WAYPOINTS     = 16015, // Waypoints | Waypoints
GFF_SAVEGAME_AREA_MAP           = 16016, // Area Map | Map of the Area
GFF_SAVEGAME_AREA_STORES        = 16017, // Stores | Stores
GFF_SAVEGAME_AREA_ROOMS_VIEWED  = 16018, // Rooms Viewed | Rooms Viewed in the Area
GFF_SAVEGAME_AREA_SOUNDS        = 16019, // Sounds | Sound emitters
GFF_SAVEGAME_AREA_MIN_CREATURE_IMPORTANCE = 16020, // Min Creature Importance In Save File | Min Creature Importance In Save File

// Area object properties
GFF_SAVEGAME_AREA_PLACEABLE_STATE        = 16100, // Placeables State | Placeable's State
GFF_SAVEGAME_AREA_TRIGGER_GEOMETRY       = 16101, // Trigger Geometry | Trigger Geometry
GFF_SAVEGAME_AREA_PLACEABLE_USEABLE      = 16102, // Placeables useable | Placeable useable
GFF_SAVEGAME_AREA_TRIGGER_DETECTABLE     = 16103, // Trigger Detectable | Trigger Trap is detectable
GFF_SAVEGAME_AREA_TRIGGER_DISARMABLE     = 16104, // Trigger Disarmable | Trigger Trap is disarmable
GFF_SAVEGAME_AREA_TRIGGER_DCDETECTCHECK  = 16105, // Trigger Detect Check | Trigger Trap Detection Difficulty
GFF_SAVEGAME_AREA_TRIGGER_DCDISARMCHECK  = 16106, // Trigger Disarm Check | Trigger Trap Disarm Difficulty
GFF_SAVEGAME_AREA_TRIGGER_LAST_DISARMED  = 16107, // Trigger Disarmed By | Trigger Trap Disarmed by Object_id
GFF_SAVEGAME_AREA_TRIGGER_REVERB_PRESET  = 16108, // Trigger Reverb Preset | Trigger Reverb Preset
GFF_SAVEGAME_AREA_TRIGGER_PRIORITY       = 16109, // Trigger Reverb Priority | Trigger Reverb Priority
GFF_SAVEGAME_AREA_TRIGGER_LOAD_SCREEN    = 16110, // Trigger Load Screen Id | Trigger Load Screen Id
GFF_SAVEGAME_AREA_TRIGGER_SOUNDS         = 16111, // Trigger sounds list | Trigger sounds list
GFF_SAVEGAME_AREA_TRIGGER_TYPE           = 16112, // Trigger type | Trigger type

GFF_SAVEGAME_AREA_TRIGGER_MUSICVOLUME_ENTERSTATE      = 16113, // music volume enter state | music volume enter state
GFF_SAVEGAME_AREA_TRIGGER_MUSICVOLUME_EXITSTATE       = 16114, // music volume exit state | music volume exit state
GFF_SAVEGAME_AREA_TRIGGER_MUSICVOLUME_ENTERSTATEDELAY = 16115, // music volume exit state delay | music volume exit state delay 
GFF_SAVEGAME_AREA_TRIGGER_MUSICVOLUME_EXITSTATEDELAY  = 16116, // music volume exit state delay | music volume exit state delay 

// Stores
GFF_SAVEGAME_STORE_MARKDOWN         = 16150,    // Store Mark Down | Store Mark Down
GFF_SAVEGAME_STORE_MARKUP           = 16151,    // Store Mark Up | Store Mark Up
GFF_SAVEGAME_STORE_GOLD             = 16152,    // Store Gold | Store Gold
GFF_SAVEGAME_STORE_MAXBUYPRICE      = 16153,    // Store Max Buy Price | Store Max Buy Price
GFF_SAVEGAME_STORE_WILLNOTBUY       = 16154,    // Store Will-Not-Buy List | Store Will-Not-Buy List
GFF_SAVEGAME_STORE_WILLONLYBUY      = 16155,    // Store Will-Only-Buy List | Store Will-Only-Buy List
GFF_SAVEGAME_STORE_ITEMLIST         = 16156,    // Store Item List | Store Item List

// Object properties, creature item lists, Party properties, etc.

// *** WARNING - somebody has mixed the ID groups between 16200 and 16300
// I know this is really ugly but keep the ids in numeric order (we used to group them
// logically but then people were creating duplicate IDs even with warning comments
// saying to be careful of this).
 
//GFF_SAVEGAME_PLAYERCHAR_AREA      = 16200, // Player's Area | The area the player's character is in.
GFF_SAVEGAME_OBJECT_ACTIVE        = 16201, // Object Active | If the object is enabled & running AI or not.
//GFF_SAVEGAME_OBJECT_AILEVEL       = 16202, // Object AI Level | The overridden AI level set by scripting.

// Party information
GFF_SAVEGAME_PARTYMEMBERS         = 16203, // Party Pool Member Status | Status of the Party Pool Members (active, inactive, etc.).
GFF_SAVEGAME_PARTYPOOLMEMBERS     = 16204, // Party Pool Members | Complete list of members in the party pool (active, inactive, etc.).
GFF_SAVEGAME_PARTYMEM_CREATURE    = 16205, // Creature info | Party member creature information.
GFF_SAVEGAME_PARTYMEM_TEMPLATE    = 16206, // Template | Party member template.
GFF_SAVEGAME_PARTYCREATURES       = 16207, // Party Creatures | The actual creatures in either pool, or party.
GFF_SAVEGAME_PLAYERCHAR_CHAR      = 16208, // Player's Character | The Main character for the player.
// (continued at 16270)

// Creature information/equipment
GFF_SAVEGAME_CREATURE_STATS       = 16209, // Creature Stats | Creature Stats
GFF_SAVEGAME_BACKPACK             = 16210, // Backpack | Backpack
GFF_SAVEGAME_PLOTITEMS            = 16211, // Plot Items | Plot Items
GFF_SAVEGAME_MONEY                = 16212, // Total Money | Total Money
GFF_SAVEGAME_QUICKITEMS           = 16213, // Quick Items | Quick Items
GFF_SAVEGAME_EQUIPMENT            = 16214, // Equipment | Equipment
GFF_SAVEGAME_EQUIPMENTSET         = 16215, // Equipment set | The set of equipment.
GFF_SAVEGAME_EQUIPMENTSET_SLOT    = 16216, // Equipment slot | Which slot is this piece of equipment in.
GFF_SAVEGAME_EQUIPMENTSET_OBJECT  = 16217, // Equipment object | Which object is in this slot.
GFF_SAVEGAME_EQUIPMENT_ACTIVESET  = 16218, // Active Equipment Set | Active Equipment Set
GFF_SAVEGAME_EQUIPMENT_ITEMS      = 16219, // Items List | The items in the equipment set.

// Object properties
GFF_SAVEGAME_OBJECT_IMMORTAL      = 16220, // Object Immortal | The object is immortal or not.
GFF_SAVEGAME_OBJECT_EVENTSCRIPT   = 16221, // Object Event Script | The changed event script for the object.
GFF_SAVEGAME_OBJECT_TAG           = 16222, // Object TAG | The TAG for the object.

// Item properties
GFF_SAVEGAME_ITEMS                = 16223, // Items | A list of items.
GFF_SAVEGAME_ITEM_DROPPABLE       = 16224, // Item Droppable | True if the item is droppable
GFF_SAVEGAME_ITEM_DAMAGED         = 16225, // Item Damaged | Damaged items cannot be equipped
GFF_SAVEGAME_MAX_ITEMS            = 16226, // Max Inventory Size | Maximum inventory slots
GFF_SAVEGAME_CRAFTING_RECIPE_LIST = 16227, // Known Crafting Recipes | Known Crafting Recipes
GFF_SAVEGAME_ITEM_IRREMOVABLE     = 16228, // Item Irremovable | Irremovable items cannot be removed by the player once equipped
GFF_SAVEGAME_ITEM_INDESTRUCTIBLE  = 16229, // Item Indestructible | Indestructible items cannot be destroyed by the player
GFF_SAVEGAME_ITEM_MATERIALTYPE    = 16230, // Material Type | Dynamic scaling may change item's material using the material progression 2DA
GFF_SAVEGAME_ITEM_STEALABLE       = 16231, // Item Stealable | True if the item is Stealable
GFF_SAVEGAME_ITEM_INFINITE        = 16232, // Infinite | True if a store has infinite stock of this item
GFF_SAVEGAME_ITEM_CURRENT_VFX_PROPERTY_ID = 16233, // Property ID causing the active VFX on the item
GFF_SAVEGAME_ITEM_CURRENT_VFX_PROPERTY_POWER = 16234, // Power of property causing the active VFX on the item

// Object properties (con't.)
GFF_SAVEGAME_OBJECT_PLOT          = 16250, // Object Plot | If the object marked as a plot object.
GFF_SAVEGAME_OBJECT_HEALTH        = 16251, // Object Health | Health of the object.
GFF_SAVEGAME_OBJECT_MAX_HEALTH    = 16252, // Object Max Health | Max health of the object.
GFF_SAVEGAME_OBJECT_RANK          = 16253,  // Object Rank | Rank of the object.
GFF_SAVEGAME_OBJECT_TREASURE_GROUP  = 16254, // Object Treasure Group | Treasure Group of the object.
GFF_SAVEGAME_OBJECT_NAME          = 16255, // Object Name | Non-localized name override.
GFF_SAVEGAME_OBJECT_LOOPING_ANIMATION = 16256, // Object Looping Animation | Looping animation of the object.
GFF_SAVEGAME_OBJECT_LOOTABLE_CREATURE_APPEARANCETYPE = 16257, // Body bag placeables need this to figure out the dead corpse model name to use
GFF_SAVEGAME_OBJECT_PICKLOCK      = 16258,  // Object picklock | Picklock difficulty level of the object.
GFF_SAVEGAME_OBJECT_TRAP_DETECTED = 16259,  // Object Trap Detected | Is a trap dected on this object ?
GFF_SAVEGAME_OBJECT_DCDETECTCHECK = 16260, // Object Trap Detect Check | Trap Detection Difficulty on this object
GFF_SAVEGAME_OBJECT_DCDISARMCHECK = 16261, // Object Trap Disarm Check | Trap Disarm Difficulty on this object
GFF_SAVEGAME_OBJECT_INTERACTION_RADIUS = 16262, // Object Interaction Radius | Used for pathfinding typically with merchants
GFF_SAVEGAME_OBJECT_IMPORTANCE    = 16263, // Object Importance | Importance of the object to the area and game (used to cut non-essential elements from low end systems)

// Party information (con't.)
GFF_SAVEGAME_SELECTED_CHARACTER   = 16270, // Selected Character | Object ID of the selected character
//GFF_SAVEGAME_FOLLOWER_LAST_ENABLED_AREA         = 16271, // Follower's Last Enabled Area | Last enabled area of a follower.
//GFF_SAVEGAME_FOLLOWER_LAST_ENABLED_POSITION     = 16272, // Follower's Last Enabled Area Position | Last enabled area position of a follower.
//GFF_SAVEGAME_FOLLOWER_LAST_ENABLED_ORIENTATION  = 16273, // Follower's Last Enabled Area Orientation | Last enabled area orientation of a follower.
GFF_SAVEGAME_PARTY_PICKER_GUI_STATUS            = 16274, // GUI status of the Party Picker
GFF_SAVEGAME_PARTY_APPROVAL_LIST  = 16275, // Party approval list | list of party members' approval of the hero
GFF_SAVEGAME_PARTY_APPROVAL_ID    = 16276, //  Approval ID | ID of party member having a certain approval
GFF_SAVEGAME_PARTY_APPROVAL_LEVEL  = 16277, // Approval level | A party member's approval level of the hero
GFF_SAVEGAME_PARTY_LEADER         = 16278, // Party Leader | Leader of the party
GFF_SAVEGAME_NONPARTYMEMBERS	  = 16279, // Non Party Members | List of members in the NON party pool.
GFF_SAVEGAME_PARTY_MEMBER_SUBSTATE  = 16280, // Party Member sub state | Substate of a party member
GFF_SAVEGAME_PARTY_MEMBER_LOCKED    = 16281, // Party Member locked state | Locked state of a party member
GFF_SAVEGAME_PARTY_MEMBER_FOLLOW    = 16282, // Party Member follow state | Follow state of a party member
GFF_SAVEGAME_PARTY_ITEM_STORAGE_ITEM        = 16284, // Party Item Storage Item | Party Item put in storage
GFF_SAVEGAME_PARTY_ITEM_STORAGE_OWNER       = 16285, // Party Item Storage Original Owner | Original owner of party item put in storage
GFF_SAVEGAME_PARTY_ITEM_STORAGE_SLOT        = 16286, // Party Item Storage Slot | Slot of party item put in storage
GFF_SAVEGAME_PARTY_ITEM_STORAGE_WEAPONSET   = 16287, // Party Item Storage Weapon Set | Weapon set of party item put in storage
GFF_SAVEGAME_PARTY_ITEM_STORAGE_LIST        = 16288, // Party Item Storage List | List of party items put in storage
GFF_SAVEGAME_PARTY_NEW_ITEM_ID              = 16289, // New Item ID | ID number of the new item
GFF_SAVEGAME_PARTY_NEW_ITEM_LIST            = 16290, // New Item List | List containing items marked "new"
GFF_SAVEGAME_PARTY_AUTO_LEVEL_DEFAULT       = 16291, // Auto level-up default | the auto level-up setting applied to characters as they join the party
GFF_SAVEGAME_PARTY_QUICKBAR_LOCKED          = 16292, 
GFF_SAVEGAME_PARTY_HOLD_POSITIONS           = 16293, 
GFF_SAVEGAME_PARTY_RUN_IN_DRIVE_MODE        = 16294, // Run in DRive Mode | Determine if the character runs or walks in drive mode

// Map options
GFF_SAVEGAME_PLAYER_MAP_ZOOM	  = 16295, // Map zoom level | Area map zoom level
GFF_SAVEGAME_PLAYER_MAP_LEGEND	  = 16296, // Legend | Area map legend visibility

GFF_SAVEGAME_PARTY_APPROVAL_DESC = 16297, // Approval description | Description of party member's approval rating
GFF_SAVEGAME_PLAYER_TIME_PLAYED  = 16298, // Time played | Accumulated time played.
GFF_SAVEGAME_PARTY_BACKPACK_SORT = 16299, // Backpack sort | Sort type of the party's backpack

// Creature stats
GFF_SAVEGAME_STATPROPERTY_BASE    = 16300, // Creature Stats Property Base | Creature Stats Property Base
GFF_SAVEGAME_STATPROPERTY_MODIFIER= 16301, // Creature Stats Property Modifier | Creature Stats Property Modifier
GFF_SAVEGAME_STATPROPERTY_CURRENT = 16302, // Creature Stats Property Current | Creature Stats Property Current
GFF_SAVEGAME_STATPROPERTY_COMREGEN= 16303, // Creature Stats Property Combat Regen | Creature Stats Property Combat Regen
GFF_SAVEGAME_STATPROPERTY_REGEN   = 16304, // Creature Stats Property Non Combat Regen | Creature Stats Property Non Combat Regen 
// (continued at 16350)

// Spells, talents, quick slots, etc.
GFF_SAVEGAME_SPELLLIST            = 16305, // Creature Spell List | Creature Spell List
GFF_SAVEGAME_TALENTLIST           = 16306, // Creature Talent List | Creature Talent List
GFF_SAVEGAME_SKILLLIST            = 16307, // Creature Skill List | Creature Skill List
GFF_SAVEGAME_QUICKSLOTS           = 16308, // Creature Quickslot Ability List | Creature Quickslot Ability List
GFF_SAVEGAME_ABILITYLIST          = 16309, // Creature Ability List | Includes spells, talents, skills and item abilities
GFF_SAVEGAME_QBAR_EXPANSION_VALUE = 16310, // Qbar Expansion Value | Amount the players quickbar is expanded.
GFF_SAVEGAME_QUICKSLOT_ABILITY    = 16311, // Quickslot Ability | Ability assigned to a quickslot.
GFF_SAVEGAME_QUICKSLOT_ITEMTAG    = 16312, // Quickslot Item tag | Name of item linked to the ability in the quickslot (if it exists).
GFF_SAVEGAME_QUICKSLOTS1          = 16313, // Creature Quickslot Ability List 1| Creature Quickslot Ability List 1
GFF_SAVEGAME_QUICKSLOTS2          = 16314, // Creature Quickslot Ability List 2| Creature Quickslot Ability List 2
GFF_SAVEGAME_QUICKSLOTS3          = 16315, // Creature Quickslot Ability List 3| Creature Quickslot Ability List 3
GFF_SAVEGAME_QUICKSLOTS4          = 16316, // Creature Quickslot Ability List 4| Creature Quickslot Ability List 4
GFF_SAVEGAME_CURENTQBAR           = 16317, // Current Quick bar | Indicates which quickbar is currently selected
GFF_SAVEGAME_LOCKQBAR             = 16318, // Lock Quick bar | Indicates if the quickbar is locked for the player
GFF_SAVEGAME_QUICKSLOT_TEMPLATE   = 16319, // Item Reference Template | A reference to an item template to recover item information if the item was deleted.

// Appearance
GFF_SAVEGAME_APPEARANCE           = 16320, // Appearance Information | Appearance Information
GFF_SAVEGAME_APPEARANCE_TYPE      = 16321, // Appearance Type | Base Appearance Type
GFF_SAVEGAME_APPEARANCE_GENDER    = 16322, // Appearance Gender | Gender of Appearance
GFF_SAVEGAME_APPEARANCE_GORE      = 16324, // Appearance Gore Level | Gore Level of Appearance
GFF_SAVEGAME_APPEARANCE_DECAPITATED               = 16325, // Appearance Decapitation Status | Decapitation Status of Appearance
GFF_SAVEGAME_APPEARANCE_ITEM_HERALDRY_VARIATION   = 16326, // Appearance Item Heraldry Variations | Appearance Item Heraldry Variations
GFF_SAVEGAME_APPEARANCE_ORIGINAL_TYPE             = 16327, // Appearance Original Type | The initial appearance type
GFF_SAVEGAME_APPEARANCE_MORPH_NAME                = 16328, // Appearance morph | Morph file

GFF_SAVEGAME_AUTOLEVELUP                          = 16329, // Auto-LevelUp setting | false if this creature doesn't use auto-levelup
//GFF_SAVEGAME_PROMPTAUTOLEVELUP                    = 16330, // Prompt for Auto-LevelUp setting | false if the user should not be prompted
GFF_SAVEGAME_QUICKSLOT_NUMBER                     = 16331, // Quickslot Number| The number of the position in the quickslot bar.

// Player portrait
GFF_SAVEGAME_PLAYER_PORTRAIT_PITCH                = 16332, // Player portrait pitch
GFF_SAVEGAME_PLAYER_PORTRAIT_YAW                  = 16333, // Player portrait yaw
GFF_SAVEGAME_PLAYER_PORTRAIT_TINT                 = 16334, // Player portrait tint
GFF_SAVEGAME_PLAYER_PORTRAIT_EXPRESSION           = 16335, // Player portrait expression
GFF_SAVEGAME_PLAYER_PORTRAIT_DISTANCE             = 16336, // Player portrait distance from camera
GFF_SAVEGAME_PLAYER_PORTRAIT_POSITIONH            = 16337, // Player portrait position horizontal
GFF_SAVEGAME_PLAYER_PORTRAIT_POSITIONV            = 16338, // Player portrait position vertical

// Creature lists of various sorts
// (continued from 16304)
GFF_SAVEGAME_STATLIST             = 16350, // Creature Stats List | Creature Stats List
GFF_SAVEGAME_HEROIC_STATLIST      = 16351, // The heroic stat list | The heroic stat list for the player and individual followers
GFF_SAVEGAME_HEROIC_PARTY_STATLIST = 16352,// The heroic stat list for the party | The heroic stat list for the party
GFF_SAVEGAME_STATPROPERTY_INDEX   = 16353, // Creature Stats Property Index | Creature Stats Property Index
//GFF_SAVEGAME_STATPROPERTY_MIN     = 16354, // Creature Stats Property Min | Creature Stats Property Min
//GFF_SAVEGAME_STATPROPERTY_MAX     = 16355, // Creature Stats Property Max | Creature Stats Property Max

// Plots
GFF_SAVEGAME_PLOT_MANAGER         = 16400, // Plot manager | Plot manager
GFF_SAVEGAME_PLOT_LIST            = 16401, // Plot Flag List | Plot Flag List
GFF_SAVEGAME_PLOT_GUID            = 16402, // Plot Flag GUID | Plot Flag GUID
GFF_SAVEGAME_PLOT_FLAGS_1         = 16403, // Plot Flag Flags 1 | Plot Flag Flags 1
GFF_SAVEGAME_PLOT_FLAGS_2         = 16404, // Plot Flag Flags 2 | Plot Flag Flags 2
GFF_SAVEGAME_PLOT_FLAGS_3         = 16405, // Plot Flag Flags 3 | Plot Flag Flags 3
GFF_SAVEGAME_PLOT_FLAGS_4         = 16406, // Plot Flag Flags 4 | Plot Flag Flags 4

GFFSTRUCT_SAVEGAME_ADDIN_UID      = 16420, // Addin UID | Addin UID
GFFSTRUCT_SAVEGAME_ADDIN_ENUS     = 16421, // Addin Name ENUS | Addin Name ENUS
GFFSTRUCT_SAVEGAME_ADDIN_FRFR     = 16422, // Addin Name FRFR | Addin Name FRFR
GFFSTRUCT_SAVEGAME_ADDIN_ITIT     = 16423, // Addin Name ITIT | Addin Name ITIT
GFFSTRUCT_SAVEGAME_ADDIN_DEDE     = 16424, // Addin Name DEDE | Addin Name Dutch
GFFSTRUCT_SAVEGAME_ADDIN_ESES     = 16425, // Addin Name ESES | Addin Name ESES
GFFSTRUCT_SAVEGAME_ADDIN_PLPL     = 16426, // Addin Name PLPL | Addin Name PLPL
GFFSTRUCT_SAVEGAME_ADDIN_RURU     = 16427, // Addin Name RURU | Addin Name RURU
GFFSTRUCT_SAVEGAME_ADDIN_PSEUDO   = 16428, // Addin Name Pseudo | Addin Name Pseudo
GFFSTRUCT_SAVEGAME_ADDIN_CSCZ     = 16429, // Addin Name CSCZ | Addin Name CSCZ
GFFSTRUCT_SAVEGAME_ADDIN_HUHU     = 16430, // Addin Name HUHU | Addin Name HUHU

// Creature groups and teams
GFF_SAVEGAME_GROUP_LIST           = 16450, // Group List | Group List
GFF_SAVEGAME_GROUP_ID             = 16451, // Group ID | Group ID
GFF_SAVEGAME_GROUP_HOSTILES       = 16452, // Group Hostility List | Group Hositlity List
GFF_SAVEGAME_TEAM_ID              = 16453, // Team ID | Team ID
GFF_SAVEGAME_CREATURE_STEALTH     = 16454, // Stealth | Creature Stealth state
GFF_SAVEGAME_IS_PLOT_GIVER        = 16455, // Plot giver | Plot giver flag
GFF_SAVEGAME_CAN_LEVELUP          = 16456, // Level up | Creature can level up.
GFF_SAVEGAME_CREATURE_TRACKABLE   = 16457, // Trackable | Creature can be tracked via Survival Skill  
GFF_SAVEGAME_CREATURE_CONTROLLABLE= 16458, // Controllable | Creature can be controlled when in the party
GFF_SAVEGAME_CREATURE_INTERACTIVE = 16459, // Interactive | Creature can be selected or acted upon
GFF_SAVEGAME_CREATURE_RACE        = 16460, // Race | Creature's current race
GFF_SAVEGAME_CREATURE_PACKAGE     = 16461, // Package | Creature's package
GFF_SAVEGAME_CREATURE_PACKAGE_AI  = 16462, // Package AI | Creature's package ai
GFF_SAVEGAME_CREATURE_CANCHANGEEQUIPMENT =  16463,  // Can Change Equipment | Creature can change equipment using the GUI
GFF_SAVEGAME_CREATURE_CLASS_RANK_LIST = 16464, // Class rank list | list of held class(es) and ranks in them
GFF_SAVEGAME_CREATURE_CLASS_ID    = 16465, // Class ID | ID of a class in a class/rank pair
GFF_SAVEGAME_CREATURE_CLASS_RANK  = 16466, // Rank | Ranks in a held class
GFF_SAVEGAME_CREATURE_IS_GHOST    = 16467, // Ghost creatures can go through regular creatures (but not other ghosts)
GFF_SAVEGAME_CREATURE_MODAL_ABILITY_LIST = 16468,  // List of active modal abilities
GFF_SAVEGAME_CREATURE_SHOW_AS_ALLY_ON_MAP = 16469,  // Show as ally on map | Creature appears on minimap as blue dot
GFF_SAVEGAME_CREATURE_IS_STATUE = 16470,  // Statue creatures have their animations paused
GFF_SAVEGAME_CREATURE_MINIMIZED_SKILL_HEADER_LIST = 16471, // Minimized skill header list | List of headers minimized in skills GUI
GFF_SAVEGAME_CREATURE_MINIMIZED_TALENT_HEADER_LIST = 16472, // Minimized talent header list | List of headers minimized in talents/spells GUI
GFF_SAVEGAME_CREATURE_ABILITY_HEADER_ID = 16473, // Minimized ability header ID | ID # corresponding to an ability header
GFF_SAVEGAME_CREATURE_ITEMS_SCALED = 16474, // Are Equipped items scaled | NPCs items are scaled once based on area and PC level

GFF_SAVEGAME_CREATURE_HEATBEAT_INTERVAL = 16475, //The interval the creatures Heartbeat event is set at

GFF_SAVEGAME_CREATURE_ROAM_RADIUS = 16476, // The roaming radius of the creature
GFF_SAVEGAME_CREATURE_ROAM_CENTER = 16477, // The center of the creature's roaming circle.

GFF_SAVEGAME_CREATURE_POOL_NAME = 16478, // The name of the pool that a creature belongs to
GFF_SAVEGAME_CREATURE_POOL_AVAILABLE = 16479, // Flag to know if a pool creature is available or in use

GFF_SAVEGAME_CREATURE_NOPERMDEATH = 16480, // Indicates if the creature can be destroyed or not
GFF_SAVEGAME_CREATURE_TIMESINCEDEATH = 16481, // How much time has elapsed since the creature died

// Decay
GFF_SAVEGAME_CREATURE_TIMEBEFOREDECAY = 16499, // Global time before creatures start decaying into corpses

// World database
GFF_SAVEGAME_WORLDDATABASE        = 16500,  // World Database | World Database
GFF_SAVEGAME_WORLDDB_IDGROUP      = 16501,  // World Database ObjectID group | World Database ObjectID group
GFF_SAVEGAME_WORLDDB_LASTID       = 16502,  // World Database Last Used ID | World Database Last Used ID

// Party
GFF_SAVEGAME_PARTY_SEEN_LINES       = 16503, // Seen Conversation Lines | Lines flagged once per game that have already been seen

// Journal
GFF_SAVEGAME_JOURNAL                            = 16504, // Journal | Journal data
GFF_SAVEGAME_JOURNAL_ACTIVE_LIST                = 16505, // Active List | List of active quests in the journal
GFF_SAVEGAME_JOURNAL_COMPLETE_LIST              = 16506, // Completed list | List if completed quests in the journal
GFF_SAVEGAME_JOURNAL_TITLE                      = 16507, // Journal Title | The name of the quest
GFF_SAVEGAME_JOURNAL_TEXT                       = 16508, // Journal Text | The text of the quest
GFF_SAVEGAME_JOURNAL_PARENT_PLOT                = 16509, // Parent Plot | The parent of this plot
GFF_SAVEGAME_JOURNAL_RESREF                     = 16510, // Plot ResRef | The ResRef of this plot
GFF_SAVEGAME_JOURNAL_STORY_TEXT                 = 16511, // Story Text | Your Story So Far text that appears on the loading screen
GFF_SAVEGAME_JOURNAL_AREA_TAG                   = 16512, // Area Tag | the tag of the area this quest should be completed in
GFF_SAVEGAME_JOURNAL_PLOT_DESTINATION_LIST      = 16513, // Plot Destination List | tags of objects that are the destination of a plot
GFF_SAVEGAME_JOURNAL_PLOT_DESTINATION_TAG       = 16514, // Plot Destination Tag | tag of an object that is a plot destination
GFF_SAVEGAME_JOURNAL_PLOT_DESTINATION_GUID_LIST = 16515, // Plot Destination GUID | GUID of a plot that has a destination object
GFF_SAVEGAME_JOURNAL_CONVERSATION_LIST          = 16516, // Conversation list | list of recorded conversations
GFF_SAVEGAME_JOURNAL_CONVERSATION_LINE_LIST     = 16517, // Conversation line list | line of conversation
GFF_SAVEGAME_JOURNAL_CONVERSATION_LINE_SPEAKER  = 16518, // Conversation speaker | speaker for line of conversation
GFF_SAVEGAME_JOURNAL_CONVERSATION_LINE_TEXT     = 16519, // Conversation text | line text
GFF_SAVEGAME_JOURNAL_CONVERSATION_LINE_REPLY    = 16520, // Coversation reply | player reply
GFF_SAVEGAME_JOURNAL_UNREAD_CODEX_LIST          = 16521, // Unread codex list | unread codex entries
GFF_SAVEGAME_JOURNAL_ORPHAN_LIST                = 16522, // Orphan List | List of child plot entries with no parent
GFF_SAVEGAME_JOURNAL_QUEST_COMPLETED            = 16523, // Quest Completed | Flag indicating whether this quest has been completed
GFF_SAVEGAME_JOURNAL_QUEST_GROUP                = 16524, // Quest Group | The ResRef of the group this quest belongs to
GFF_SAVEGAME_JOURNAL_GROUP_LIST                 = 16525, // Quest Group List | List of quest groups
GFF_SAVEGAME_JOURNAL_GROUP_RESREF               = 16526, // Quest Group ResRef | Resource name of this quest group
GFF_SAVEGAME_JOURNAL_GROUP_OPEN_IN_CURRENT      = 16527, // Quest Group Open in Current | Whether this quest group is expanded in current quests
GFF_SAVEGAME_JOURNAL_GROUP_OPEN_IN_COMPLETED    = 16528, // Quest Group Open in Completed | Whether this quest group is expanded in completed quests
GFF_SAVEGAME_JOURNAL_GROUP_PRIORITY             = 16529, // Quest Group Priority | Priority controls the ordering of quest groups in the journal

// Journal continued at 16540

GFF_SAVEGAME_AMBIENTDIALOG_LIST                 = 16530, // Ambient Dialog List | List of active ambient dialogs.
GFF_SAVEGAME_AMBIENTDIALOG_OWNER                = 16531, // Ambient Dialog Owner | Owner of conversation
GFF_SAVEGAME_AMBIENTDIALOG_SPEAKER              = 16532, // Ambient Dialog Speaker | Current speaker
GFF_SAVEGAME_AMBIENTDIALOG_RESREF               = 16533, // Ambient Dialog ResRef | ResRef
GFF_SAVEGAME_AMBIENTDIALOG_LINE                 = 16534, // Ambient Dialog Line | Current line.

// Journal continued from 16529

GFF_SAVEGAME_JOURNAL_QUEST_UPDATED              = 16540, // Quest Updated | Whether this quest has changed recently
GFF_SAVEGAME_JOURNAL_OFFER_ID                   = 16541, // Offer Id | The PRC Offer Id associated with the plot

// Body bag
GFF_SAVEGAME_BODYBAG_ID             = 16600, // Bodybag ID | The ID of the object's bodybag
GFF_SAVEGAME_ISBODYBAG              = 16601, // IsBodyBag | True if the placeable is a bodybag
GFF_SAVEGAME_LOOTABLE_OBJECT_ID     = 16602, // Lootable Object ID | The ID of the object the bodybag belongs to

// Save game AoE data
GFF_SAVEGAME_AOE_ID                 = 16603, // AoE ID | Type of AoE
GFF_SAVEGAME_AOE_SHAPE              = 16604, // AoE Shape | Shape of the AoE (Sphere, Rectangle, Cone)
GFF_SAVEGAME_AOE_RADIUS             = 16605, // AoE Radius | Radius of AoE, for sphere shapes
GFF_SAVEGAME_AOE_WIDTH              = 16606, // AoE Width | Width of AoE, for rectangle shapes
GFF_SAVEGAME_AOE_LENGTH             = 16607, // AoE Length | Length of AoE, for rectangle shapes
GFF_SAVEGAME_AOE_CREATOR            = 16608, // AoE Creator ID | Id Of object which created the AoE
GFF_SAVEGAME_AOE_DURATION           = 16609, // AoE Duration | Duration of the AoE
GFF_SAVEGAME_AOE_DURATION_TYPE      = 16610, // AoE Duration Type | Type of duration (instant, temporary, permanent)
GFF_SAVEGAME_AOE_LINKED             = 16611, // AoE link flag | True if AoE is linked to a creature (moves with it)
// GFF_SAVEGAME_AOE_ABILITY_ID      = 16750  // << Careful, this is defined below.... Other AOE variables defined after 16750

// more creature data
GFF_SAVEGAME_CREATURE_RANK         =  16612,  // Creature Rank | creatureranks.xls idx, Exported as 'guibar' from the toolset for some reason.

// Save game Game Effect data
GFF_SAVEGAME_EFFECT_ID              = 16613, // Game Effect ID | ID of the game effect
GFF_SAVEGAME_EFFECT_TYPE            = 16614, // Game Effect Type | Type of game effect
GFF_SAVEGAME_EFFECT_DURATION_TYPE   = 16615, // Game Effect Duration Type | Duration type of the game effect
GFF_SAVEGAME_EFFECT_DURATION        = 16616, // Game Effect Duration | Duration of the game effect
GFF_SAVEGAME_EFFECT_SUBTYPE         = 16617, // Game Effect Sub Type | Sub Type of the game effect
GFF_SAVEGAME_EFFECT_TIMEINDEX       = 16618, // Game Effect Time Index | elapsed time of the game effect
GFF_SAVEGAME_EFFECT_ANIMATION       = 16619, // Game Effect Animation ID | ID of the animation of the game effect
GFF_SAVEGAME_EFFECT_PRIORITY        = 16620, // Game Effect Priority | Priority of the game effect
GFF_SAVEGAME_EFFECT_CREATOR         = 16621, // Game Effect Creator ID | ID of the creator of the game effect
GFF_SAVEGAME_EFFECT_ABILITY_ID      = 16622, // Game Effect Ability ID | ID of the ability that created the game effect
GFF_SAVEGAME_EFFECT_LIST            = 16623, // Game Effect List | List of game effects
GFF_SAVEGAME_EFFECT_ENGINE_DATA     = 16624, // Game Effect Engine data | Additional engine specific data for the game effect
GFF_SAVEGAME_EFFECT_RESOURCE2       = 16625, // Game Effect Resource2 | A linked resource that is saved elsewhere
GFF_SAVEGAME_EFFECT_STARTINGID      = 16626, // Last gameeffect ID | Indicates the starting ID of the gameeffects
GFF_SAVEGAME_EFFECT_FLAGS           = 16627, // Game Effect Flags | Stores the flags an effect has activated.


// Save game AI Master data
GFF_SAVEGAME_AI_MASTER              = 16636, // AI Master | The current AI Master state
GFF_SAVEGAME_EVENT_QUEUE            = 16630, // AI Event Queue | Queue of the AI events in the AI Master
GFF_SAVEGAME_EVENT_DAY              = 16631, // AI Event Day | Day of the event
GFF_SAVEGAME_EVENT_TIME             = 16632, // AI Event Time | Time of the event
GFF_SAVEGAME_EVENT_CALLER_ID        = 16633, // AI Event Caller ID | ID of the event caller
GFF_SAVEGAME_EVENT_TARGET_ID        = 16634, // AI Event Target ID | ID of the event target
GFF_SAVEGAME_EVENT_ID               = 16635, // AI Event ID | ID of the event

// Save game data arrays
GFF_SAVEGAME_DATAARRAY              = 16640, // Data Arrays | Data Array struct
GFF_SAVEGAME_DATAARRAY_INT          = 16641, // Data Arrays | Data Arrays integer list
GFF_SAVEGAME_DATAARRAY_FLOAT        = 16642, // Data Arrays | Data Arrays float list
GFF_SAVEGAME_DATAARRAY_BOOL         = 16643, // Data Arrays | Data Arrays bool list
GFF_SAVEGAME_DATAARRAY_OID          = 16644, // Data Arrays | Data Arrays OBJECT_ID list
GFF_SAVEGAME_DATAARRAY_STRING       = 16645, // Data Arrays | Data Arrays string list
GFF_SAVEGAME_DATAARRAY_VECTOR       = 16646, // Data Arrays | Data Arrays vector list
GFF_SAVEGAME_DATAARRAY_QUATERNION   = 16647, // Data Arrays | Data Arrays quaternion list

// Save game AI Event data
GFF_SAVEGAME_EVENT_SCRIPT           = 16650, // Event script | Script information for an event
GFF_SAVEGAME_EVENT_SIMPLE_VALUE     = 16651, // Event simple value | Simple value for an event (single object id, etc.)

// Save game script data
GFF_SAVEGAME_SCRIPT_EVENT_TYPE      = 16670, // Script Event Type | Type of the script event
GFF_SAVEGAME_SCRIPT_EVENT_CREATOR   = 16671, // Script Event Creator | Creator of the script event
GFF_SAVEGAME_SCRIPT_EVENT_TARGET    = 16672, // Script Event Target | Target of the script event
GFF_SAVEGAME_SCRIPT_EVENT_DATA      = 16673, // Script Event Data | Data of the script event
GFF_SAVEGAME_SCRIPT_EVENT_SCRIPT_NAME   = 16674, // Script Event Script Name | Script name of the script event
GFF_SAVEGAME_SCRIPT_EVENT_RESOURCE_LIST = 16675, // Script Event Resource List | Resource list of the script event

// World timer
GFF_SAVEGAME_WORLD_TIMER            = 16700, // World Timer | World Timer
GFF_SAVEGAME_WORLD_TIMER_DAY        = 16701, // World Timer Day | Day of the World Timer
GFF_SAVEGAME_WORLD_TIMER_TIME       = 16702, // World Timer Time | Time of the World Timer

// Waypoints
GFF_SAVEGAME_WAYPOINT_MAPNOTE           = 16710,  // Waypoint Map Note | Does this waypoint have a map note
GFF_SAVEGAME_WAYPOINT_MAPNOTE_ENABLED   = 16711,  // Waypoint Map Note Enabled | Enabled status of the map note for this waypoint
// This field is being left in for backwards compatibility with old save game (expires March 8, 2009)
GFF_SAVEGAME_WAYPOINT_MAPNOTE_TEXT      = 16712,  // Waypoint Map Note Text | Text of the map note for this waypoint
GFF_SAVEGAME_WAYPOINT_MAPNOTE_TYPE      = 16713,  // Waypoint Map Note Type | Type of the map note for this waypoint
GFF_SAVEGAME_WAYPOINT_MAPNOTE_LOC_TEXT  = 16714,  // Waypoint Map Note Loc Text | Localized text of the map note for this waypoint

// Commandlist
GFF_SAVEGAME_CURRENT_COMMAND        = 16720, // Current Command | Current Command
GFF_SAVEGAME_COMMAND_LIST           = 16721, // Command List | Command List
GFF_SAVEGAME_COMMAND_COMMANDID      = 16722, // Command Command ID | Command Command ID
GFF_SAVEGAME_COMMAND_ID             = 16723, // Command ID | Command ID
GFF_SAVEGAME_COMMAND_STATIC         = 16724, // Command Static | Command Static
GFF_SAVEGAME_COMMAND_DATA           = 16725, // Command Data | Command Data
GFF_SAVEGAME_COMMAND_PLAYERISSUED   = 16726, // Player Issued

// Subactions
GFF_SAVEGAME_SUBACTION_LIST                 = 16730, // Sub Action List | List of Sub Actions
GFF_SAVEGAME_SUBACTION_ID                   = 16731, // Sub Action ID | The ID of the Sub Action
GFF_SAVEGAME_SUBACTION_CORE_SUBACTION       = 16732, // Sub Action Core | Is this the core Sub Action?
GFF_SAVEGAME_SUBACTION_CORE_INTERRUPTABLE   = 16733, // Sub Action Interruptable | Is this Sub Action interruptable?
GFF_SAVEGAME_SUBACTION_TIME_INDEX           = 16734, // Sub Action Time Index | Sub Action Time Index
GFF_SAVEGAME_SUBACTION_LAST_TIME_INDEX      = 16735, // Sub Action Last Time Index | Sub Action Last Time Index
GFF_SAVEGAME_SUBACTION_LENGTH               = 16736, // Sub Action Length | The ID of the Sub Action
GFF_SAVENAME_SUBACTION_START_TIME           = 16737, // Sub Action Start Time | Sub Action Start Time
GFF_SAVEGAME_SUBACTION_DATA                 = 16738, // Sub Action Data | The data of the Sub Action

// Action Queue
GFF_SAVEGAME_CURRENT_ACTION_QUEUE           = 16740, // Current Action Queue | The current action queue on an object

// AoE objects, continued...
GFF_SAVEGAME_AOE_ABILITY_ID                = 16750,    // AOE Ability ID | Ability ID that created the AoE object
GFF_SAVEGAME_AOE_FLAGS                     = 16751,    // AOE Flag | A flag variable for the AOE
GFF_SAVEGAME_AOE_STATIONARY                = 16752,    // AOE Stationary | Stationary AoEs mark the pathfinding patches so creatures try to avoid them

// Savegame version info (number, package dependencies, etc.)
GFF_SAVEGAME_BUILD_NUMBER                   = 16770, // Build Number | The private build number from this save.
GFF_SAVEGAME_SAVE_VERSION_INTERNAL          = 16771, // Internal Save Version Number | The save version number used internally by the development team.

GFF_SAVEGAME_WORLDMAP                       = 16780, // World Map | struct for world map
GFF_SAVEGAME_WORLDMAP_PRIMARYMAP            = 16781, // Primary Map | tag of primary map
GFF_SAVEGAME_WORLDMAP_SECONDARYMAP          = 16782, // Secondary Map | tag of secondary map
GFF_SAVEGAME_WORLDMAP_MAPLIST               = 16783, // Map list | list of map objects
GFF_SAVEGAME_WORLDMAP_MAP_TAG               = 16784, // Map tag | tag of map object
GFF_SAVEGAME_WORLDMAP_MAP_PLAYERLOC         = 16785, // Player loc | location of player on the world map
GFF_SAVEGAME_WORLDMAP_MAP_PINLIST           = 16786, // Pin list | list of map pins
GFF_SAVEGAME_WORLDMAP_MAPPIN_TAG            = 16787, // Pin tag | tag of the map pin
GFF_SAVEGAME_WORLDMAP_MAPPIN_STATE          = 16788, // Pin state | state of the map pin
GFF_SAVEGAME_WORLDMAP_MAPPIN_RECENTLY_ACTIVATED = 16789, // Recently activated | true when pin made active, until viewed
GFF_SAVEGAME_WORLDMAP_GUI_STATUS            = 16790, // World Map GUI Status | Can the user see/use the world map?
GFF_SAVEGAME_WORLDMAP_LAST_PIN_CLICKED      = 16791, // Last world map pin clicked
GFF_SAVEGAME_WORLDMAP_MAPPIN_ACTIVATED_PREVIOUSLY = 16792, // Whether this pin has been activated in the past
GFF_SAVEGAME_WORLDMAP_MAPPIN_LAST_STATE     = 16793, // the pin's previous state
GFF_SAVEGAME_WORLDMAP_TRAVELPOINT_POSX      = 16794, // Position X | position X of the travel point
GFF_SAVEGAME_WORLDMAP_TRAVELPOINT_POSY      = 16795, // Position Y | position Y of the travel point
GFF_SAVEGAME_WORLDMAP_MAP_TRAVELPATH_BEFORE = 16796, // Travel Path Before | list of points to travel before random encounter
GFF_SAVEGAME_WORLDMAP_MAP_TRAVELPATH_AFTER  = 16797, // Travel Path After | list of points to travel after random encounter
GFF_SAVEGAME_WORLDMAP_MAPPIN_NAME           = 16798, // Pin name | name of the map pin

// save meta data
GFF_SAVEGAME_META_AREANAME                  = 16800, // Area name | Name of current area.
GFF_SAVEGAME_META_TIMEPLAYED                = 16801, // Time played | Seconds played.
GFF_SAVEGAME_META_LEVEL                     = 16802, // Level | Hero's level
GFF_SAVEGAME_META_CLASS                     = 16803, // Class | Hero's class
GFF_SAVEGAME_META_GENDER                    = 16804, // Gender | Hero's gender
GFF_SAVEGAME_META_RACE                      = 16805, // Race | Hero's race
GFF_SAVEGAME_META_BACKGROUND                = 16806, // Background | Hero's background
GFF_SAVEGAME_META_NAME                      = 16807, // Name | Hero's name
GFF_SAVEGAME_META_SAVENAME                  = 16808, // Savegame name | Save name


// Party tactics
GFF_SAVEGAME_TACTICENTRY_TARGET_OBJECT_ID   = 16818, // Tactic target object ID | Object ID of the object that the tactic target refers to
GFF_SAVEGAME_TACTICENTRY_CONDITION_OBJECT_ID= 16819, // Tactic condition object ID | Object ID of the object that the tactic condition refers to
GFF_SAVEGAME_PARTY_TACTICS_ITEM_ABILITIES   = 16820, // Tactics item abilities | item abilities for tactics interface
GFF_SAVEGAME_TACTICS_HAS_TABLE              = 16821, // Has tactics table | Creature has a tactics table
GFF_SAVEGAME_TACTICS_TABLE                  = 16822, // Tactics table | struct for tactics table
GFF_SAVEGAME_TACTICS_ENABLED                = 16823, // Tactics enabled | tactics enabled for creature
GFF_SAVEGAME_TACTICS_LIST                   = 16824, // Tactics list | list of tactics entries
GFF_SAVEGAME_TACTICENTRY_ENABLED            = 16825, // Entry enabled | Tactic entry is enabled
GFF_SAVEGAME_TACTICENTRY_TARGET             = 16826, // Tactic target | Target of the tactic
GFF_SAVEGAME_TACTICENTRY_CONDITION          = 16827, // Tactic condition | Condition to evaluate for the tactic
GFF_SAVEGAME_TACTICENTRY_COMMAND            = 16828, // Tactic command | Command for the tactic
GFF_SAVEGAME_TACTICENTRY_COMMANDPARAM       = 16829, // Tactic command parameter | Command parameter for the tactic
GFF_SAVEGAME_TACTICENTRY_TARGETTAG          = 16830, // Tactic target tag | Tag of the object that the tactic target refers to
GFF_SAVEGAME_TACTICENTRY_CONDITIONTAG       = 16831, // Tactic condition tag | Tag of the object that the tactic condition refers to
GFF_SAVEGAME_TACTICS_DIRTY                  = 16832, // Tactics dirty
GFF_SAVEGAME_TACTICS_PRESETTYPE             = 16833, // Tactics preset type
GFF_SAVEGAME_TACTICS_PRESETINDEX            = 16834, // Tactics preset index
GFF_SAVEGAME_TACTICS_PRESETLIST             = 16835, // Tactics preset list
GFF_SAVEGAME_TACTICS_CUSTOMLIST             = 16836, // Tactics custom list
GFF_SAVEGAME_TACTICENTRY_COMMANDITEMTAG     = 16837,
GFF_SAVEGAME_TACTICENTRY_COMMANDITEMRESREF  = 16838,

// Plot actions
GFF_SAVEGAME_PLOTACTIONS                    = 16840, // Plot actions | Plot actions control
GFF_SAVEGAME_PLOTACTIONS_ENABLED            = 16841, // Plot actions enabled | enabled state
GFF_SAVEGAME_PLOTACTIONS_CURRENTSET         = 16842, // Current set | current action set
GFF_SAVEGAME_PLOTACTIONS_LIST               = 16843, // Actions list | list of all plot actions
GFF_SAVEGAME_PLOTACTION_ID                  = 16844, // Plot action id | Unique identifier of plot action
GFF_SAVEGAME_PLOTACTION_STATE               = 16845, // Plot action state | current state of plot action
GFF_SAVEGAME_PLOTACTION_COUNT               = 16846, // Plot action count | current count value of plot action
GFF_SAVEGAME_PLOTACTION_UPDATED             = 16847, // Plot action updated | Whether the plot action is updated

// Sounds object properties
GFF_SAVEGAME_SOUND_TAG                   = 16900, // Sound object tag | sound object tag
GFF_SAVEGAME_SOUND_ACTIVE                = 16901, // Sound active flag | is sound active 
GFF_SAVEGAME_SOUND_NAME                  = 16902, // Sound event name | sound event name
GFF_SAVEGAME_SOUND_XPOSITION             = 16903, // sound position X | sound position X
GFF_SAVEGAME_SOUND_YPOSITION             = 16904, // sound position Y | sound position Y
GFF_SAVEGAME_SOUND_ZPOSITION             = 16905, // sound position Z | sound position Z
GFF_SAVEGAME_SOUND_XORIENTATION          = 16906, // sound orientation X | sound orientation X
GFF_SAVEGAME_SOUND_YORIENTATION          = 16907, // sound orientation Y | sound orientation Y
GFF_SAVEGAME_SOUND_ZORIENTATION          = 16908, // sound orientation Z | sound orientation Z
GFF_SAVEGAME_SOUND_WORIENTATION          = 16909, // sound orientation W | sound orientation W
GFF_SAVEGAME_SOUND_VOLUME                = 16910, // sound volume | sound volume
GFF_SAVEGAME_SOUND_PITCH                 = 16911, // sound pitch | sound pitch
GFF_SAVEGAME_SOUND_FADEIN                = 16912, // sound fade in | sound fade in
GFF_SAVEGAME_SOUND_FADEOUT               = 16913, // sound fade out | sound fade out
GFF_SAVEGAME_SOUND_MAXDISTANCEMULT       = 16914, // sound max distance multiplier | sound max distance multiplier
GFF_SAVEGAME_SOUND_CONEINSIDE            = 16915, // sound inside cone | sound inside cone
GFF_SAVEGAME_SOUND_CONEOUTSIDE           = 16916, // sound outside cone | sound outside cone
GFF_SAVEGAME_SOUND_CONEVOLUME            = 16917, // sound cone volume | sound cone volume
GFF_SAVEGAME_SOUND_PRIORITY              = 16918, // sound priority | sound priority
GFF_SAVEGAME_SOUND_OCCLUDABLE            = 16919, // sound occludable flag | is sound occludable flag

GFF_SAVEGAME_PLAYER_MORPH                = 16950, // Head morph for main player
GFF_SAVEGAME_PLAYER_SOUNDSET             = 16951, // current player creature soundset
GFF_SAVEGAME_DEFAULT_SOUNDSET            = 16952, // default (from GFF) player creature soundset

// Add-Ins
GFF_SAVEGAME_ADDIN_NAME                  = 16960, // Add-In Name | Add-In Name

// Story So Far.
GFF_SAVEGAME_STORYSOFAR_EVENTLIST		= 16970, // Story So Far Event List | List of Events tracked in the hero's story so far.
GFF_SAVEGAME_STORYSOFAR_EVENTID			= 16971, // Story So Far Event ID | The event Id for each event tracked in the hero's story (so far).
GFF_SAVEGAME_STORYSOFAR_GAMETIME		= 16972, // Story So Far Game Time | The In Game Time that the Story So Far event occurred at.
GFF_SAVEGAME_STORYSOFAR_UTC				= 16973, // Story So Far UTC | The real world time that the STory So Far event occurred at.
GFF_SAVEGAME_STORYSOFAR_SCREENSHOT		= 16974, // Story So Far Screen Shot | The screen shot (if any) associated with this event Id for the hero's story (so far).
GFF_SAVEGAME_STORYSOFAR_LEVELUPLIST     = 16975, // Story So Far Level Up Stats | The Level Up stats of the hero's at each level up event.

GFF_SAVEGAME_STORYSOFAR_AREA			= 16976, // Story So Far Area Name for Level Up Stats | The Area that the hero was in during level up.
GFF_SAVEGAME_STORYSOFAR_LEVEL			= 16977, // Story So Far Hero Level | The Level of the hero's at each level up event.
GFF_SAVEGAME_STORYSOFAR_MONEY			= 16978, // Story So Far Hero Money | The hero's money at each level up event.
GFF_SAVEGAME_STORYSOFAR_CURRENT_HEATLH  = 16979, // Story So Far Current Health | The hero's current health at each level up event.
GFF_SAVEGAME_STORYSOFAR_TOTAL_HEATLH    = 16980, // Story So Far Total Health | The hero's total health at each level up event.
GFF_SAVEGAME_STORYSOFAR_CURRENT_STAMINA = 16981, // Story So Far Current Stamina | The hero's current stamina at each level up event.
GFF_SAVEGAME_STORYSOFAR_TOTAL_STAMINA   = 16982, // Story So Far Total Stamina | The hero's total stamina at each level up event.
GFF_SAVEGAME_STORYSOFAR_CURRENT_XP		= 16983, // Story So Far Current XP | The hero's current experisnce points at each level up event.
GFF_SAVEGAME_STORYSOFAR_SPELL_LIST      = 16984, // Story So Far Spell List | The hero's spells at each level up event.
GFF_SAVEGAME_STORYSOFAR_TALENT_LIST     = 16985, // Story So Far Talent List | The hero's talents at each level up event.
GFF_SAVEGAME_STORYSOFAR_SKILL_LIST		= 16986, // Story So Far Skill List | The hero's skills at each level up event.
GFF_SAVEGAME_STORYSOFAR_ATTRIBUTE_LIST  = 16987, // Story So Far Attribute List | The hero's attributes at each level up event.
GFF_SAVEGAME_STORYSOFAR_ATTRIBUTE_BASE	= 16988, // Story So Far Base Attribute | The hero's base attribute at each level up event.
GFF_SAVEGAME_STORYSOFAR_ATTRIBUTE_MODIFIER = 16989, // Story So Attribute Modifier | The hero's attribute modifier at each level up event.
GFF_SAVEGAME_STORYSOFAR_EQUIPMENT_LIST	= 16990,
GFF_SAVEGAME_STORYSOFAR_EQUIPMENT_SLOTID= 16991,
GFF_SAVEGAME_STORYSOFAR_EQUIPMENT_RESREF= 16992,
GFF_SAVEGAME_STORYSOFAR_EQUIPMENT_STACKSIZE = 16993,
GFF_SAVEGAME_STORYSOFAR_ITEM_PROPERTY	= 16994,
GFF_SAVEGAME_STORYSOFAR_ITEM_POWER		= 16995,
GFF_SAVEGAME_STORYSOFAR_ITEM_DATA		= 16996,

// End Save Game Range, reserved up to 16999

// Begin Designer Data/Toolset Range

// Begin Script Var Table Range
GFF_SCRIPTVARTABLE                      = 17000, // VarTable | struct list, Script Var Table
GFF_SCRIPTVARTABLE_NAME                 = 17001, // Name | WCHAR, VarTable Entry Name
GFF_SCRIPTVARTABLE_TYPE                 = 17002, // Type | BYTE, VarTable Entry Type
GFF_SCRIPTVARTABLE_VALUE                = 17003, // Value | VarTable Entry Value

// End Script Var Table Range, reserved up to 17099

// Begin Campaign Data Range
GFF_CAMPAIGN_CIF_ENTRY_AREA_LIST        = 17100, // Entry Area List | Area List that the player starts in
GFF_CAMPAIGN_CIF_ENTRY_AREA             = 17101, // Entry Area | Area that the player starts in
GFF_CAMPAIGN_CIF_ENTRY_POSITION         = 17102, // Entry Position | Position that the player starts at
GFF_CAMPAIGN_CIF_ENTRY_ORIENTATION      = 17103, // Entry Orientation | Orientation that the player starts at
GFF_CAMPAIGN_CIF_ENTRY_SCRIPT           = 17104, // Entry Script | Script that runs on module entry (server)
GFF_CAMPAIGN_CIF_ENTRY_CLIENT_SCRIPT    = 17105, // Entry Client Script | Client Script that runs on module entry
GFF_CAMPAIGN_CIF_DISPLAY_NAME_EN_US     = 17106, // Display Name | The localized display name for the module
GFF_CAMPAIGN_CIF_DISPLAY_NAME_FR_FR     = 17107, 
GFF_CAMPAIGN_CIF_DISPLAY_NAME_DE_DE     = 17108, 
GFF_CAMPAIGN_CIF_DISPLAY_NAME_PL_PL     = 17109, 
GFF_CAMPAIGN_CIF_DISPLAY_NAME_RU_RU     = 17110, 
GFF_CAMPAIGN_CIF_DISPLAY_NAME_IT_IT     = 17111, 
GFF_CAMPAIGN_CIF_DISPLAY_NAME_ES_ES     = 17112, 
GFF_CAMPAIGN_CIF_DISPLAY_NAME_HU_HU     = 17113, 
GFF_CAMPAIGN_CIF_DISPLAY_NAME_CS_CZ     = 17114, 
GFF_CAMPAIGN_CIF_DESCRIPTION_EN_US      = 17115, // Description | The localized description
GFF_CAMPAIGN_CIF_DESCRIPTION_FR_FR      = 17116,
GFF_CAMPAIGN_CIF_DESCRIPTION_DE_DE      = 17117,
GFF_CAMPAIGN_CIF_DESCRIPTION_PL_PL      = 17118,
GFF_CAMPAIGN_CIF_DESCRIPTION_RU_RU      = 17119,
GFF_CAMPAIGN_CIF_DESCRIPTION_IT_IT      = 17120,
GFF_CAMPAIGN_CIF_DESCRIPTION_ES_ES      = 17121,
GFF_CAMPAIGN_CIF_DESCRIPTION_HU_HU      = 17122,
GFF_CAMPAIGN_CIF_DESCRIPTION_CS_CZ      = 17123,
GFF_CAMPAIGN_CIF_PACKAGES_LIST          = 17124, // Packages List | The list of required packages for the module
// End Campaign Data Range, reserved up to 17599

// End Designer Data/Toolset Range, reserved up to 18999

// Begin Talk table range

GFF_TALK_BUCKET_LIST                     = 19000, // Bucket List | List of buckets in the hash table
GFF_TALK_STRING_LIST                     = 19001, // String List | List of strings inside each bucket
GFF_TALK_STRING_ID                       = 19002, // String ID | The string ID of the string
GFF_TALK_STRING                          = 19003, // String | The string value of the string

// End Talk Table range, reserved up to 19999

// Begin Placeable pathfinding grid patches

GFF_PLACEABLE_STATES_LIST                = 20000, // States List | List of state patches 
// End Placeable pathfinding grid patches, reserved up to 20999

// Begin VFX project files range 
GFF_VFX_CHILD_LIST						= 21000, // Child list | VFX editor child list
GFF_VFX_OBJECT_ID						= 21001, // VFX Object ID | VFX Object ID
GFF_VFX_EMITTER_INITIALROTATIONRANGE	= 21002, // Emitter Parameter | Emitter Parameter
//GFF_VFX_ORIENTATION						= 21003, // Orientation | Orientation of an object in the VFX editor
GFF_VFX_ROOT           					= 21004, // Root | Root object in VFX editor
GFF_VFX_EMITTER_MESH_PARTICLE_ROLL_AXIS = 21005, // Roll Axis| Roll axis for chunky particles
GFF_VFX_TYPE   					        = 21006, // VFX Type | The type of vfx this vfx is
GFF_VFX_OBJECT_VISIBLE 				    = 21007, // VFX Render Object Visible | VFX Render Object Visible
GFF_VFX_EMITTER_MESH_PARTICLE_UP_AXIS   = 21008, // Spawn Axis | Spawn axis for chunky particles
GFF_VFX_KEYFRAME   					    = 21009, // Keyframe | Keyframe in a list of animation values
GFF_VFX_VALUE   					    = 21010, // Value | Value for a given keyframe
GFF_VFX_EMITTER_NAME					= 21011, // Emitter | Emitter object in VFX editor
GFF_VFX_EMITTER_TYPE  		            = 21012, // Emitter Type | Type of emitter
GFF_VFX_EMITTER_ORIENTATIONBEHAVIOUR  	= 21013, // Orientation Behaviour | Behaviour of the orientation
GFF_VFX_EMITTER_UPDATEONLYWHENVISIBLE   = 21014, // Emitter Parameter | Emitter Parameter
GFF_VFX_EMITTER_LINKPARTICLESTOGETHER   = 21015, // Emitter Parameter | Emitter Parameter
GFF_VFX_EMITTER_MATERIALLIBRARY 	    = 21016, // Emitter Parameter | Emitter Parameter
GFF_VFX_EMITTER_MATERIALOBJECT		    = 21017, // Emitter Parameter | Emitter Parameter
GFF_VFX_EMITTER_BIRTHRATE  		        = 21018, // Emitter Parameter | Emitter Parameter
GFF_VFX_EMITTER_BIRTHRATERANGE  		= 21019, // Emitter Parameter | Emitter Parameter
GFF_VFX_EMITTER_BIRTHRATEINPARTICLESPERMETER  	= 21020, // Emitter Parameter | Emitter Parameter
GFF_VFX_EMITTER_INITIALSPEED  		    = 21021, // Emitter Parameter | Emitter Parameter
GFF_VFX_EMITTER_INITIALSPEEDRANGE  	    = 21022, // Emitter Parameter | Emitter Parameter
GFF_VFX_EMITTER_ACCELERATION            = 21023, // Emitter Parameter | Emitter Parameter
GFF_VFX_EMITTER_GRAVITYMULTIPLIER       = 21024, // Emitter Parameter | Emitter Parameter
GFF_VFX_EMITTER_LIFE                    = 21025, // Emitter Parameter | Emitter Parameter
GFF_VFX_EMITTER_LIFERANGE               = 21026, // Emitter Parameter | Emitter Parameter
GFF_VFX_EMITTER_SCALERANGE              = 21027, // Emitter Parameter | Emitter Parameter
GFF_VFX_EMITTER_SPREADX                 = 21028, // Emitter Parameter | Emitter Parameter
GFF_VFX_EMITTER_SPREADY                 = 21029, // Emitter Parameter | Emitter Parameter
GFF_VFX_EMITTER_INITIALROTATIONSPEED    = 21030, // Emitter Parameter | Emitter Parameter
GFF_VFX_EMITTER_INITIALROTATIONSPEEDRANGE           = 21031, // Emitter Parameter | Emitter Parameter
GFF_VFX_EMITTER_ROTATIONALACCELERATION              = 21032, // Emitter Parameter | Emitter Parameter
__deprecated__GFF_VFX_EMITTER_RANDOMINITIALROTATION               = 21033, // Deprecated March 20/08.  Left in for backwards-compatibility with VFXPROJ files -PjW
GFF_VFX_EMITTER_PARTICLEINHERITANCE                 = 21034, // Emitter Parameter | Emitter Parameter
GFF_VFX_EMITTER_INHERITVELOCITYINSTEADOFPOSITION    = 21035, // Emitter Parameter | Emitter Parameter
GFF_VFX_EMITTER_PARTICLESAFFECTEDBYWIND             = 21036, // Emitter Parameter | Emitter Parameter
GFF_VFX_EMITTER_ENABLEPARTICLECOLLISIONS            = 21037, // Emitter Parameter | Emitter Parameter
GFF_VFX_EMITTER_PHYSICSOBJECTSPAWN                  = 21038, // Emitter Parameter | Emitter Parameter
GFF_VFX_EMITTER_PHYSICSEMITTER                      = 21039, // Emitter Parameter | Emitter Parameter
GFF_VFX_EMITTER_MOVEMENTSPREADX                     = 21040, // Emitter Parameter | Emitter Parameter
GFF_VFX_EMITTER_MOVEMENTSPREADY                     = 21041, // Emitter Parameter | Emitter Parameter
GFF_VFX_EMITTER_MOVEMENTSPREADUPDATEDELAY           = 21042, // Emitter Parameter | Emitter Parameter
GFF_VFX_EMITTER_TARGETNAME                          = 21043, // Emitter Parameter | Emitter Parameter
GFF_VFX_EMITTER_TARGETATTRACTION                    = 21044, // Emitter Parameter | Emitter Parameter
GFF_VFX_EMITTER_TARGETRADIUS                        = 21045, // Emitter Parameter | Emitter Parameter
GFF_VFX_EMITTER_SPAWNDIRECTIONTRACKSTARGET          = 21046, // Emitter Parameter | Emitter Parameter
GFF_VFX_EMITTER_KILLPARTICLEWHENTARGETHIT           = 21047, // Emitter Parameter | Emitter Parameter
GFF_VFX_EMITTER_PARTICLESFOLLOWPATH                 = 21048, // Emitter Parameter | Emitter Parameter
GFF_VFX_EMITTER_FLIPBOOK_TYPE						= 21049, // Emitter Flipbook Parameter | Flipbook type
GFF_VFX_EMITTER_FLIPBOOK_FRAMES_PER_SECOND          = 21050, // Emitter Flipbook Parameter | Frames per Second
GFF_VFX_EMITTER_FLIPBOOK_ROWS						= 21051, // Emitter Flipbook Parameter | Flipbook Rows
GFF_VFX_EMITTER_FLIPBOOK_COLUMNS					= 21052, // Emitter Flipbook Parameter | Flipbook Columns
GFF_VFX_EMITTER_FLIPBOOK_RANDOM_START_FRAME         = 21053, // Emitter Flipbook Parameter | Random Start Frame
GFF_VFX_EMITTER_ALPHAMULTIPLIER                     = 21054, // Emitter Parameter | Emitter Parameter
GFF_VFX_EMITTER_COLORMULTIPLIER                     = 21055, // Emitter Parameter | Emitter Parameter
GFF_VFX_EMITTER_SCALEMULTIPLIER                     = 21056, // Emitter Parameter | Emitter Parameter
GFF_VFX_EMITTER_INFINITELIFE                        = 21057, // Emitter Parameter | Emitter Parameter
GFF_VFX_EMITTER_CHUNKY_MODEL_NAME					= 21058, // Emitter Parameter | Emitter Parameter
GFF_VFX_EMITTER_INITIALROTATION                     = 21059, // Emitter Parameter | Emitter Parameter

GFF_VFX_CRUSTNODE_NAME					= 21060, // Crust Node | Crust Node object in VFX editor
GFF_VFX_CRUSTNODE_REALNAME				= 21061, // Crust Node Real Name | The original name found in the mmh file
GFF_VFX_CRUSTNODE_CRUSTHOOKID           = 21062,  // Crust Node ID | The crust hook ID value
GFF_VFX_GEOMETRY_FILE_NAME				= 21063,  // Geometry File Name | External Geometry File Name

GFF_VFX_EMITTER_AGENT                   = 21064, // Struct containing the data for all the properties in CAgentVFXEmitter
GFF_VFX_USE_VARIATION_TINT              = 21065, // Flag | Flag

GFF_VFX_DUMMY_NAME					    = 21070, // Dummy Node Name | Dummy object in VFX editor

GFF_VFX_GEOMETRY_NAME					= 21080, // Geometry Name | Geometry object in VFX editor
GFF_VFX_GEOMETRY_SCALE					= 21081, // Geometry scale | scale of geometry

GFF_VFX_TARGET_NAME					    = 21090, // Target Name | Target object in VFX editor
GFF_VFX_MODEL_NAME					    = 21100, // Model Name | Reference model object in VFX editor
GFF_VFX_MODEL_RESOURCETYPE	    	    = 21101, // Resource Type | Resource type for model object in VFX editor
GFF_VFX_MODEL_ANIMATIONNAME 	        = 21102, // Animation Name | Name of animation played on reference model
GFF_VFX_CREATURE_NAME					= 21110, // Creature Name | Reference crust based  object in VFX editor
GFF_VFX_CREATURE_URI					= 21111, // Creature URI | Reference crust based  object in VFX editor

GFF_VFX_RELATIVE_POSITION_X               = 21120,  // Position X | The x coordinate of the position
GFF_VFX_RELATIVE_POSITION_Y               = 21121,  // Position Y | The Y coordinate of the position
GFF_VFX_RELATIVE_POSITION_Z               = 21122,  // Position Z | The Z coordinate of the position
GFF_VFX_RELATIVE_ORIENTATION_X            = 21123,  // Orientation X | The x coordinate of the Orientation
GFF_VFX_RELATIVE_ORIENTATION_Y            = 21124,  // Orientation Y | The Y coordinate of the Orientation
GFF_VFX_RELATIVE_ORIENTATION_Z            = 21125,  // Orientation Z | The Z coordinate of the Orientation

GFF_VFX_IMPACT_LENGTH                     = 21130,  // Impact | Length of Impact animation
GFF_VFX_DURATION_LENGTH                   = 21131,  // Duration | Length of Duration animation
GFF_VFX_CESSATION_LENGTH                  = 21132,  // Cessation | Length of Cessation animation
GFF_VFX_CUSTOM_LENGTH                     = 21133,  // Custom | Length of Custom animation
GFF_VFX_CUSTOM_NAME                       = 21134,  // Custom Name | Name of Custom animation

GFF_VFX_AGEMAP_COLOR_R                      = 21140, // Age Map Red | Age Map red color
GFF_VFX_AGEMAP_COLOR_G                      = 21141, // Age Map Green | Age Map green color
GFF_VFX_AGEMAP_COLOR_B                      = 21142, // Age Map Blue | Age Map blue color
GFF_VFX_AGEMAP_COLOR_A                      = 21143, // Age Map Alpha | Age Map alpha 
GFF_VFX_AGEMAP_SCALE_X                      = 21144, // Age Map Scale X | Age Map X scale
GFF_VFX_AGEMAP_SCALE_Y                      = 21145, // Age Map Scale Y | Age Map Y scale
GFF_VFX_AGEMAP_ROTATIONAL_SPEED_MULTIPLIER  = 21146, // Rotation Multiplier | Rotational Speed Multiplier

GFF_VFX_EVENT                             = 21150, // Emitter Event | Emitter Event
GFF_VFX_EVENT_TIME                        = 21151, // Event Time | Emitter Event
GFF_VFX_EVENT_TYPE                        = 21152, // Event Type | Emitter Event
GFF_VFX_EVENT_ID                          = 21153, // Event ID | Emitter Event
GFF_VFX_EVENT_TARGETSYSTEM                = 21154, // Target System | Emitter Event

GFF_VFX_EMITTER_VOLUME_SPAWN_TYPE                  = 21160, // Emitter Parameter | Emitter Parameter
GFF_VFX_EMITTER_VOLUME_SPAWN_SELECTED_PART_NAME    = 21161, // Emitter Parameter | Emitter Parameter
GFF_VFX_EMITTER_VOLUME_SPAWN_ARBITRARY_VOLUME_NAME = 21162, // Emitter Parameter | Emitter Parameter
GFF_VFX_EMITTER_COLLISION_TYPE					   = 21163, // Collision Type | Collision Type
GFF_VFX_EMITTER_BOUNCE_VALUE					   = 21164, // Collision Bounce Value | Collision Bounce Value
GFF_VFX_EMITTER_VOLUME_SPAWN_WITHIN_VOLUME         = 21165, // Emitter Parameter | Emitter Parameter
GFF_VFX_EMITTER_VOLUME_SPAWN_INVERT_NORMALS        = 21166, // Emitter Parameter | Emitter Parameter


GFF_VFX_EMITTER_COLORMULTIPLIER_R                  = 21170, // Emitter Parameter | Emitter Parameter
GFF_VFX_EMITTER_COLORMULTIPLIER_G                  = 21171, // Emitter Parameter | Emitter Parameter
GFF_VFX_EMITTER_COLORMULTIPLIER_B                  = 21172, // Emitter Parameter | Emitter Parameter

GFF_VFX_SPLAT_AGEMAP_COLOR_R                      = 21173, // Splat Age Map Red | Splat Age Map red color
GFF_VFX_SPLAT_AGEMAP_COLOR_G                      = 21174, // Splat Age Map Green | Splat Age Map green color
GFF_VFX_SPLAT_AGEMAP_COLOR_B                      = 21175, // Splat Age Map Blue | Splat Age Map blue color
GFF_VFX_SPLAT_AGEMAP_COLOR_A                      = 21176, // Splat Age Map Alpha | Splat Age Map alpha 
GFF_VFX_SPLAT_AGEMAP_SCALE_X                      = 21177, // Splat Age Map Scale X | Splat Age Map X scale
GFF_VFX_SPLAT_AGEMAP_SCALE_Y                      = 21178, // Splat Age Map Scale Y | Splat Age Map Y scale

GFF_VFX_FILE_OBJECT_VERSION						   = 21180, // VFX File Vesion | VFX File Version

GFF_VFX_EMITTER_SPLAT_ALPHAMULTIPLIER             = 21181, // Emitter Parameter | Emitter Parameter
GFF_VFX_EMITTER_SPLAT_COLORMULTIPLIER_R           = 21182, // Emitter Parameter | Emitter Parameter
GFF_VFX_EMITTER_SPLAT_COLORMULTIPLIER_G           = 21183, // Emitter Parameter | Emitter Parameter
GFF_VFX_EMITTER_SPLAT_COLORMULTIPLIER_B           = 21184, // Emitter Parameter | Emitter Parameter

GFF_VFX_EMITTER_VOLUME_SPAWN_PRIMITIVE_MESH_TYPE			= 21185, // Emitter Parameter | Emitter Parameter
GFF_VFX_EMITTER_VOLUME_SPAWN_PRIMITIVE_BOX_MIN				= 21186, // Emitter Parameter | Emitter Parameter
GFF_VFX_EMITTER_VOLUME_SPAWN_PRIMITIVE_BOX_MAX				= 21187, // Emitter Parameter | Emitter Parameter
GFF_VFX_EMITTER_VOLUME_SPAWN_PRIMITIVE_SPHERE_R				= 21188, // Emitter Parameter | Emitter Parameter
GFF_VFX_EMITTER_VOLUME_SPAWN_PRIMITIVE_CYLINDER_R			= 21189, // Emitter Parameter | Emitter Parameter
GFF_VFX_EMITTER_VOLUME_SPAWN_PRIMITIVE_CYLINDER_H			= 21190, // Emitter Parameter | Emitter Parameter
GFF_VFX_EMITTER_VOLUME_SPAWN_PRIMITIVE_CYLINDER_AXIS        = 21191, // Emitter Parameter | Emitter Parameter
GFF_VFX_EMITTER_VOLUME_SPAWN_USE_VOLUME_NORMAL				= 21192, // Emitter Parameter | Emitter Parameter

GFF_VFX_EMITTER_WORLD_AXIS_ACCELERATION_X			        = 21193, // Emitter Parameter | Emitter Parameter
GFF_VFX_EMITTER_WORLD_AXIS_ACCELERATION_Y			        = 21194, // Emitter Parameter | Emitter Parameter
GFF_VFX_EMITTER_WORLD_AXIS_ACCELERATION_Z			        = 21195, // Emitter Parameter | Emitter Parameter

GFF_VFX_RANGE										        = 21196, // VFX Range(Bounding Box) | VFX Range(Bounding Box)

GFF_VFX_EMITTER_AXIS_ACCELERATION_SPACE 			        = 21197, // Emitter Parameter | Emitter Parameter
GFF_VFX_EMITTER_UVDISTRIBUTIONSIZE                          = 21198, // Emitter Parameter | Emitter Parameter

GFF_VFX_EMITTER_GROUP_NAME                                  = 21210, // Emitter Group | Emitter group name

GFF_VFX_REMOTE_MATERIAL_TINT_R                              = 21220,
GFF_VFX_REMOTE_MATERIAL_TINT_G                              = 21221,
GFF_VFX_REMOTE_MATERIAL_TINT_B                              = 21222,
GFF_VFX_REMOTE_MATERIAL_TINT_A                              = 21223,
GFF_VFX_REMOTE_MATERIAL_FRESNEL_FALLOFF                     = 21224,
GFF_VFX_REMOTE_MATERIAL_INVERT_FRESNEL                      = 21225,
GFF_VFX_REMOTE_MATERIAL_ALPHA                               = 21226,
GFF_VFX_REMOTE_MATERIAL_DECAL_NAME                          = 21227,

// End VFX project files range reserved up to 21999

GFF_WND_ROOT                            = 22000, // WND file root
GFF_WND_RESREF                          = 22001, // Resref | used in ARL
GFF_WND_RADIUS                          = 22002, // float | radius of effect

GFF_WND_STRENGTH                        = 22003, // float | Strengh [0,1]
GFF_WND_DIRECTION                       = 22004, // Vec3 | Direction
GFF_WND_RADIUS_FALLOFF                  = 22005, // float | falloff for local effects

GFF_WND_GUST_MIN_STRENGTH               = 22010, // The gusting min strength [0,1]
GFF_WND_GUST_MAX_STRENGTH               = 22011, // The gusting max strength [0,1]
GFF_WND_GUST_MIN_DURATION               = 22012, // The gusting min duration
GFF_WND_GUST_MAX_DURATION               = 22013, // The gusting max strength

GFF_WND_GUST_FREQUENCY                  = 22014 , // float | freq Hz

GFF_WND_TREE_NUM_WIND_MATRICES          = 22020, // float | number of wind matrices to use in rendering
GFF_WND_TREE_NUM_LEAF_ANGLES            = 22021, // float | number of leaf angles to use in rendering
GFF_WND_TREE_RESPONSE                   = 22022, // float | wind response
GFF_WND_TREE_RESPONSE_LIMIT             = 22023, // float | response limit
GFF_WND_TREE_MAX_BEND_ANGLE             = 22024, // float | maximum bending in degrees
GFF_WND_TREE_BRANCH_EXPONENT            = 22025, // float | SPT branch exponent
GFF_WND_TREE_LEAF_EXPONENT              = 22026, // float | SPT leaf exponent

GFF_WND_TREE_BRANCH_OSCILLATION_X       = 22027, // vec4 | from speedtree cad
GFF_WND_TREE_BRANCH_OSCILLATION_Y       = 22028, // vec4 | from speedtree cad
GFF_WND_TREE_LEAF_ROCKING               = 22029, // vec4 | from speedtree cad
GFF_WND_TREE_LEAF_RUSTLING              = 22030, // vec4 | from speedtree cad

GFF_WND_CLOTH_RESPONSE                  = 22031, // float | Maximum cloth response to wind
GFF_WND_CLOTH_RESPONSE_LMT              = 22032, // float | Maximum acceleration of change of cloth response to wind
GFF_WND_CLOTH_STRENGTH                  = 22033, // float | Cloth wind strength
GFF_WND_CLOTH_GUST_STRENGTH_MIN         = 22034, // float | Minimum gusting strength for cloth
GFF_WND_CLOTH_GUST_STRENGTH_MAX         = 22035, // float | Maximum gusting strength for cloth
GFF_WND_CLOTH_GUST_DURATION_MIN         = 22036, // float | Minimum duration of gusting for cloth
GFF_WND_CLOTH_GUST_DURATION_MAX         = 22037, // float | Maximum duration of gusting for cloth
GFF_WND_CLOTH_GUST_INTERVAL_MIN         = 22038, // float | Minimum interval between gusting for cloth
GFF_WND_CLOTH_GUST_INTERVAL_MAX         = 22039, // float | Maximum interval between gusting for cloth 
GFF_WND_CLOTH_GUST_DIR_CHANGE           = 22040, // float | Maximum direction change of wind during gusting [0, 1]
GFF_WND_CLOTH_GUST_AXIS_RATIO           = 22041, // vector3 | Radio of gusting change per each component of direction

// End WND file range reserved up to 22499

GFF_ATMO_DATA                           = 22500, // list of ATMO
GFF_ATMO_SUN_COLOR                      = 22519, // vector3 | Sun color for atmosphere.
GFF_ATMO_SUN_INTENSITY                  = 22520, // float | Sun power, multiplies the extinction and in-scattering terms.
GFF_ATMO_TURBIDITY                      = 22521, // float | Turbidity factor for MIE term
GFF_ATMO_EARTH_REFLECTANCE              = 22522, // float | Extinction term (Mie) multiplier
GFF_ATMO_MIE_MULTIPLIER                 = 22523, // float | Modulates the Mie scattering term
GFF_ATMO_RAYLEIGH_MULTIPLIER            = 22524, // float | Modulates the rayleigh term
GFF_ATMO_EARTH_IN_SCATTER_POWER         = 22525, // float | Modulates the in-scatter
GFF_ATMO_DISTANCE_MULTIPLIER            = 22526, // float | modulates the distance from object to camera.
GFF_ATMO_PHASE_ECCENTRICITY             = 22527, // float | Henyey / Greenstein phase eccentricity
GFF_ATMO_ALPHA                          = 22528, // float | Amount of atmospheric influence over the level
GFF_ATMO_FOG_COLOR                      = 22529, // Vec3f | Distance-based fog color
GFF_ATMO_FOG_INTENSITY                  = 22530, // float | Distance-based fog intensity
GFF_ATMO_FOG_CAP                        = 22531, // float | Maximum fog index
GFF_ATMO_FOG_ZENITH                     = 22532, // float | Aperture angle for skybox (vertical) fog
GFF_ATMO_FOG_WATER_INTENSITY            = 22533, // float | Distance-based intensity for water planes
GFF_ATMO_FOG_WATER_CAP                  = 22534, // float | Maximum fog index for water planes
GFF_ATMO_FOG_TACTICAL_MULTIPLIER        = 22535, // float | Multiplier for fog when in full tactical camera

GFF_CLOUD_DATA                          = 22600, // list of CLDS 
GFF_CLOUD_DENSITY                       = 22620, // float | Overcast -> scatter 
GFF_CLOUD_SHARPNESS                     = 22621, // float | Controls the thickness of clouds
GFF_CLOUD_DEPTH                         = 22622, // float | Controls the virtual heightmap offset.
GFF_CLOUD_RANGE_MULTIPLIER1             = 22623, // float | Multiplies the cloud texture coords.
GFF_CLOUD_RANGE_MULTIPLIER2             = 22624, // float | Multiplies the cloud texture coords.
GFF_CLOUD_COLOR                         = 22625, // vector3 | Cloud tinting color.

GFF_MOON_SCALE                          = 22700, // float | Scale for the moon (or sun) in the sky
GFF_MOON_ALPHA                          = 22701, // float | Alpha for the moon in the sky
GFF_MOON_CLOUDALPHA                     = 22702, // float | Alpha for the moon as reflected by the clouds
GFF_MOON_ROTATION                       = 22703, // float | Rotation for moon (or sun or fade tear) in the sky 


// End ATMO/CLOUD file range reserved up to 22999

GFF_MORPH_PARTS                  =   23000, // Morph parts | Parts composing the morphed head
GFF_MORPH_TINTFILENAMES          =   23001, // Tints | Tint file names
GFF_MORPH_NODES                  =   23002, // Nodes | List of morphed nodes
GFF_MORPH_TEXTURE_NAME           =   23003, // Texture | Texture name for material parameter
GFF_MORPH_TEXTUREPARAM           =   23004, // Textures | Texture material parameter list
GFF_MORPH_VECTOR4FPARAM          =   23005, // Vectors | Vector material parameter list
GFF_MORPH_FLOATPARAM             =   23006, // Floats | Float material parameter list
GFF_MORPH_FLOATPARAMVALUE        =   23007, // Float | Float material parameter value
GFF_MORPH_NAME                   =   23008, // String | Morph name
GFF_MORPH_MAT_NODE_NAME          =   23009, // String | Node name for material
GFF_MORPH_MAT_PARAM_NAME         =   23010, // String | Parameter name for material
GFF_MORPH_MAT_PARAM_INDEX        =   23011, // Int | Parameter's index for material
GFF_MORPH_MAT_PARAM_VALUE        =   23012, // Float | Parameter's value for material
GFF_MORPH_MAT_PARAM_VECTOR       =   23013, // vector4 | Parameter's vector for material
GFF_MORPH_MAT_PARAMS             =   23014, // Struct list | Material's parameters list
GFF_MORPH_MAT_VEC_PARAMS         =   23015, // Struct list | Material's parameters list
GFF_MORPH_MODEL_NAME             =   23016, // String | Model's name
GFF_MORPH_MODEL_VALUE            =   23017, // Float32 | Model's parameter value
GFF_MORPH_MODEL_PARAMS           =   23018, // Struct list | Model's parameters list
GFF_MORPH_TEX_NODE_NAME          =   23019, // String | Node name for texture
GFF_MORPH_TEX_PARAM_NAME         =   23020, // String | Parameter name for texture
GFF_MORPH_TEX_NAME               =   23021, // String | Texture name
GFF_MORPH_TEXTURES               =   23022, // Struct list | Textures


// End MORPH file range reserved up to 23999

GFF_MAP_TAG                     = 24000, // Tag | Tag name of a map
GFF_MAP_TYPE                    = 24001, // Type | 2DA index of the map type
GFF_MAP_PINLIST                 = 24002, // Pin list | List of map pins
GFF_MAP_PIN_STATE               = 24003, // State | State of the map pin
GFF_MAP_PIN_POS_X               = 24004, // X | x position of map pin
GFF_MAP_PIN_POS_Y               = 24005, // Y | y position of map pin
GFF_MAP_PIN_NAME                = 24006, // Name | Name of map pin
GFF_MAP_PIN_TAG                 = 24007, // Tag | Tag of map pin
GFF_MAP_PIN_AREATAG             = 24008, // Area tag | Tag of associated area
GFF_MAP_PIN_TERRAINTYPE         = 24009, // Terrain | Terrain type of area
GFF_MAP_PIN_TYPE                = 24010, // Type | Type of map pin
GFF_MAP_MAPS                    = 24011, // Maps | List of map objects
GFF_MAP_MAP_PARENT_RESREF       = 24012, // ParentMap ResRef | string, ResRef of Parent Map (for PRC)
GFF_MAP_PIN_WAYPOINT_OVERRIDE   = 24013, // WaypointOverride | Optional tag for target waypoint in target area
GFF_MAP_TRAILLIST               = 24014, // Trail list | List of map trails
GFF_MAP_TRAIL_PIN_1_TAG         = 24015, // Pin 1 Tag | Pin 1's tag
GFF_MAP_TRAIL_PIN_2_TAG         = 24016, // Pin 2 Tag | Pin 1's tag
GFF_MAP_POINTLIST               = 24017, // Point list | List of map trail points
GFF_MAP_POINT_POS_X             = 24018, // X | x position of map trail point
GFF_MAP_POINT_POS_Y             = 24019, // Y | y position of map trail point
GFF_MAP_PIN_TOOLTIP             = 24020, // Tooltip | Tooltip of map pin

// End MAP file range reserved up to 24999

GFF_DEP_FILE_LIST                = 25000,  // FileList | list of files+dependencies
GFF_DEP_RESREF                   = 25001,  // Name | string, resref of file
GFF_DEP_DEPENDENCY_LIST          = 25002,  // DependencyList | string list of dependencies

// End DEP range reserved up to 25099

GFF_CHAR_MOP                    = 250100,  // MOP structure
GFF_CHAR_APP                    = 250101,  // Appearance structure
GFF_CHAR_GENDER                 = 250102,  // Gender
GFF_CHAR_RACE                   = 250103,  // Race
GFF_CHAR_CLASS                  = 250104,  // Class
GFF_CHAR_BACK                   = 250105,  // Background
GFF_CHAR_ATTRIBUTES             = 250106,  // List of attributes
GFF_CHAR_ABILITIES              = 250107,  // List of abilities
GFF_CHAR_NAME                   = 250108,  // Character name
GFF_CHAR_HEAD_NAME              = 250109,  // Character's head name
GFF_CHAR_ATTRIBUTE_ID           = 250110,  // Attribute ID
GFF_CHAR_ATTRIBUTE_POINTS       = 250111,  // Attribute points
GFF_CHAR_PORTRAIT               = 250112,  // Portrait data

// End CHAR range reserved up to 25199

GFF_SAVEPROFILE_BUILD_NUMBER            = 26000, // Build Number | Build number during last save event.
GFF_SAVEPROFILE_INITIAL_BUILD_NUMBER    = 26001, // Initial Build Number | Build number when the file was originally created.
GFF_SAVEPROFILE_LAST_USED_PROFILE		= 26002, // Last Used Profile | The profile that was last loaded/saved.
GFF_SAVEPROFILE_PROFILELIST				= 26003, // Profile List | List of Different account Profiles.
GFF_SAVEPROFILE_ACCOUNT_NAME			= 26004, // Account Name | Account Name associated with this profile.
GFF_SAVEPROFILE_LOCAL_ACHIEVEMENT_DATA	= 26005, // Achievement Data | Additional Achievement Data for this account profile.
GFF_SAVEPROFILE_ACHIEVEMENTLIST			= 26006, // Achievement List | List of Achievements for this account profile.
GFF_SAVEPROFILE_ACHIEVEMENT_ID			= 26007, // Achievement ID | The ID of this Achievement.
GFF_SAVEPROFILE_ACHIEVEMENT_NEW			= 26008, // New Achievement | Indicates if this achievement should appear as newly unlocked on the gui.
GFF_SAVEPROFILE_ACHIEVEMENT_ONLINE		= 26009, // Online Achievement | Indicates if this achievement should appears as online on the gui.
GFF_SAVEPROFILE_ACHIEVEMENT_COUNT		= 26010, // Achievement Count | The value stored for this achievement.
GFF_SAVEPROFILE_ACHIEVEMENT_DATE		= 26011, // Achievement Unlock Date | The date/time that this achievement was unlocked.

GFF_SAVEPROFILE_ADDIN_LIST				= 26100, // Addin List | List of AddIns 
GFF_SAVEPROFILE_OFFER_LIST				= 26101, // Offer List | List of Offers 
GFF_SAVEPROFILE_CONTENT_NAME			= 26102, // Content Name | The name of the add-in
GFF_SAVEPROFILE_CONTENT_SHOWN			= 26103, // Content Shown | If the content has been shown yet on the gui
GFF_SAVEPROFILE_CONTENT_ENABLED         = 26104, // Content Enabled | The enable status of the add-in
GFF_SAVEPROFILE_CONTENT_TOKEN			= 26105, // Content Auth Token | The token used to verify this add-in if purchased
GFF_SAVEPROFILE_CONTENT_USER			= 26106, // Content User | The user who bought this add-in if purchased
GFF_SAVEPROFILE_FILE_LIST				= 26107, // Content File List | List of files in the add-in that are protected files
GFF_SAVEPROFILE_FILE_NAME				= 26108, // Content File Name | File within the add-in that is protected
GFF_SAVEPROFILE_FILE_DATA				= 26109, // Content File Data | Additional data needed to open a protected file in an add-in
GFF_SAVEPROFILE_FILE_VERSION			= 26110, // Content File Version | Version of the add-in
GFF_SAVEPROFILE_ADDIN_TOKEN_LIST        = 26111  // Addin Token List | List of AddIn Tokens
// End SAVEPROFILE range reserved up to 26199

};

#endif // BINARYGFFIDLIST_H
"""

from os.path import join, dirname
import re

_field_name_by_id = {}
_field_id_by_name = {}

def _read_field_names():
    pattern = re.compile(r'(?:__deprecated__)?[GC]FF(?:STRUCT)?_(\w*)\s*=\s*(\d+)')
    for line in _BinaryGFFIDList_h.splitlines():
        m = pattern.match(line)
        if m:
            name = m.group(1)
            id = int(m.group(2))
            _field_name_by_id[id] = name
            _field_id_by_name[name] = id
            globals()[name] = id
_read_field_names()

del join, dirname, re, _read_field_names, _BinaryGFFIDList_h

def get_field_name(id):
    return _field_name_by_id.get(id, id)

def get_field_id(name):
    return _field_id_by_name[name]